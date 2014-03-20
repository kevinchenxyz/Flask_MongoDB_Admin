#-*- encoding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, HiddenField,SelectField
from wtforms.validators import Required, ValidationError
from model import User
#~ from wtforms.csrf import CSRF
import hashlib

class AddUserForm(Form):
    account = TextField(u'請輸入帳號', validators=[Required(message=u'帳號請勿空白')])
    pwd = TextField(u'請輸入密碼', validators=[Required(message=u'密碼請勿空白')])
    email = TextField(u'請輸入email', validators=[Required(message=u'email請勿空白')])
    name = TextField(u'請輸入暱稱')

    def validate_account(self, field):
        if field.data == None:
            raise ValidationError(u"請輸入帳號")

    def validate_pwd(self, field):
        if field.data == None:
            raise ValidationError(u'請輸入密碼')



class LoginForm(Form):
    account = TextField(u"帳號", validators=[Required(message=u"請輸入帳號")])
    pwd = PasswordField(u"密碼",validators=[Required(message=u"請輸入密碼")])
    name = TextField(u"暱稱")


    def _get_user(self):
        try:
            user = User.objects(account=self.account.data).first()
        except MultipleObjectsReturned: #if two sections have the same name
            user = user[0]
        return user

    def validate_account(self, field):
        if self._get_user() is None:
            raise ValidationError(u"該使用者不存在")


    def validate_pwd(self, field):
        user = self._get_user()
        #~ generate_csrf_token()
        field.data_md5 = hashlib.md5()# use hashlib.md5
        field.data_md5.update(field.data) # to md5
        md5_pwd = field.data_md5.hexdigest()
        if user and user.pwd != md5_pwd:
            raise ValidationError(u'密碼不正確')

class ModifyForm(Form):
    set__account = TextField(u"帳號", validators=[Required(message=u"請輸入帳號")])
    set__pwd = TextField(u"密碼",validators=[Required(message=u"請輸入密碼")])
    set__name = TextField(u"暱稱")
    set__email = TextField(u'email')


    obj_id = HiddenField(u'uid', validators=[Required(message=u"uid 值不得為空")])#作用為何
    def validate_set__account(self, field):
      if field.data is None:
        raise ValidationError(u"帳號不得為空")

    def validate_set__pwd(self, field):
      raise ValidationError(u"密碼不得為空")

    def validate_obj_id(self, field):#method 與validator 有何不同
        if field.data is None:
            raise(u"uid 值不得為空")
