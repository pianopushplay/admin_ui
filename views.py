from flask_admin import Admin, AdminIndexView, helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask import redirect, render_template, request, url_for, abort
from models import *
from app import app, db

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create customized model view class
class dgBaseView(ModelView):

    column_display_pk = True
    page_size = 20
    can_view_details = True
    #can_export = False
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


class regularRbacView(dgBaseView):

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
            return True
        
        return False


class SuperView(dgBaseView):

    can_export = True

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            #self.can_export = True
            return True
        return False

class PianoAdminIndexView(AdminIndexView):
    """
    This does the trick rendering the view only if the user is authenticated
    """
    column_display_pk = True
    page_size = 20
    can_view_details = True
    
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

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

@app.route('/')
def index():
    return render_template('index.html')


admin = Admin(
    app, 
    name='pianos', 
    template_mode='bootstrap3',
    base_template='piano_master.html',
    )


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


admin.add_view(SuperView(User, db.session))
admin.add_view(SuperView(Role, db.session))
admin.add_view(ModelView(Piano, db.session))
