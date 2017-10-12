from flask_admin import Admin, AdminIndexView, helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask import redirect, render_template, request, url_for, abort
from models import *
from app import app, db

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='admin2@gmail.com', password='admin2')
#     db.session.commit()
# 
# @app.route('/login')
# @login_required
# def login():
#     return redirect('/admin')




class PianoAdminIndexView(AdminIndexView):
    """
    This does the trick rendering the view only if the user is authenticated
    """
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
    index_view=PianoAdminIndexView())


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


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Piano, db.session))
