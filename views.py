import os
import os.path as op

from flask_admin import Admin, AdminIndexView, form, expose, helpers as admin_helpers
from flask_admin.form import SecureForm, rules
from flask_admin.contrib.sqla import ModelView

from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user

from flask import redirect, render_template, request, url_for, abort, jsonify

from sqlalchemy.event import listens_for

from jinja2 import Markup



from models import *
from app import app, db

from flask_restful import Resource, Api
api = Api(app)


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )




# Create customized model view class
class BaseViewAdmin(ModelView):
    form_base_class = SecureForm
    column_display_pk = True
    page_size = 20
    can_view_details = True
    can_export = True

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class SuperuserViewAdmin(BaseViewAdmin):
    def is_accessible(self):
        # set accessibility...
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        # roles with ascending permissions...
        if current_user.has_role('superuser'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return True
        return False


class VolunteerViewAdmin(BaseViewAdmin):
    can_export = False
    def is_accessible(self):
        # set accessibility...
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        # roles with ascending permissions...
        if current_user.has_role('superuser'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return True

        if current_user.has_role('volunteer'):
            self.can_edit = True
            self.can_delete = False
            self.can_create = False
            self.can_export = False
            return True
        return False


class PianoViewAdmin(VolunteerViewAdmin):
    edit_template = 'piano/edit_piano.html'
    create_template = 'piano/create_piano.html'
    list_template = 'piano/list_piano.html'


class RoleViewAdmin(SuperuserViewAdmin):
    column_searchable_list = ['name']


image_path = op.join(op.dirname(__file__), 'static/images')
class ImageViewAdmin(VolunteerViewAdmin):
    # list_template = "image/list_image.html"

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename='images/'+form.thumbgen_filename(model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=image_path,
                                      thumbnail_size=(100, 100, True))
    }



@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(image_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(image_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass



admin = Admin(
    app,
    name='pianos',
    template_mode='bootstrap3',
    base_template='piano_master.html',
    )

admin.add_view(SuperuserViewAdmin(User, db.session))
admin.add_view(RoleViewAdmin(Role, db.session))
admin.add_view(PianoViewAdmin(Piano, db.session))
admin.add_view(ImageViewAdmin(Image, db.session))


# pianos api
class PianoList(Resource):
    def get(self):
        pianos = Piano.query.filter_by(active=True)
        pianosJson = {}
        for piano in pianos:
            piano.name = piano.title.split("@")
            pianosJson[piano.name[0]] = piano.json_dump()
        return jsonify(pianosJson)

api.add_resource(PianoList, '/api/v1.0/pianos')



@app.route('/')
def index():
    pianos = Piano.query.filter_by(active=True)
    return render_template('index.html', pianos=pianos)
