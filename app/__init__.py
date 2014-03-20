#-*- encoding:utf-8 -*-

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine
import os


app = Flask(__name__)

#~ if os.path.exists("/etc/oxexam_online/admin_cfg.py"):
    #~ os.environ['YOURAPPLICATION_SETTINGS'] = '/etc/oxexam_online/admin_cfg.py'
    #~ app.config.from_envvar('YOURAPPLICATION_SETTINGS')
#~ else:
app.config.from_object('config')
    
    
db = MongoEngine(app)

get_dict = lambda dct, *keys: {key: dct[key] for key in keys}

def register_blueprints(app):

    from app.users import users
    from app.admin import admin
    app.register_blueprint(users)
    app.register_blueprint(admin)

register_blueprints(app)

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(userid):
    return model.User.objects.with_id(userid)


from app import model
