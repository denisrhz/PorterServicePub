from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, url_for, request

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Admin #
from app.models import Message, City, Service, User, Role

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class MessageAdminView(AdminMixin, ModelView):
    form_columns = ['author', 'phone', 'body', 'service', 'city']

class CityAdminView(AdminMixin, ModelView):
    pass

class ServiceAdminView(AdminMixin, ModelView):
    pass

class FileAdminView(AdminMixin, FileAdmin):
    pass

path = op.join(op.dirname(__file__), 'static', 'images')

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))

admin.add_view(MessageAdminView(Message, db.session))
admin.add_view(ServiceAdminView(Service, db.session))
admin.add_view(CityAdminView(City, db.session))
admin.add_view(FileAdminView(path, name='Static Files'))

# Security #
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from app import routes, models