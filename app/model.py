#-*- encoding:utf-8 -*-

from app import db
from flask.ext.login import UserMixin

class User(db.Document, UserMixin):
    """
    Flask Mongoengine Schema User
    """
    account = db.StringField(max_length=25, required=True)
    pwd = db.StringField(max_length=25, required=True)
    name = db.StringField(max_length=25)
    email = db.EmailField(max_length=50)
    meta = {
            'collection': 'users'
    }

    def get_id(self):
        return unicode(self.id)


