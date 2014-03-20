#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from forms import AddUserForm, ModifyForm
from flask.views import MethodView
from model import User
from app import app, get_dict
from flask.ext.login import login_required
from flask.ext.mongoengine import ValidationError
from mongoengine import NotUniqueError
import hashlib

admin = Blueprint('admin', __name__, template_folder='templates')

class ListView(MethodView):

    @login_required
    def get(self):
        form = AddUserForm()
        mform = ModifyForm()
        users = User.objects
        return render_template('admin.html',
            users=users, form=form,
            mform=mform, errors=request.args,
            version = app.config['VERSION'])
        return render_template('topbar.html',users=users)
    
    @login_required
    def post(self):
        errors=dict()
        action=request.args.get('action')
        
        def dict2str(get_dict):
                this_list = get_dict.values()
                return this_list[0]
            
        if action=='add':
            user_dict = get_dict(request.form, 'account', 'pwd', 'name', 'email' )
            try:
                User(**user_dict).save()
            except ValidationError as e:
                return redirect(url_for('admin.list',**e.errors))

            except:
                errors=dict({"unique":u"帳號重複請重新輸入"})
                return redirect(url_for('admin.list',**errors))

        if action=='modify':
            user_dict=get_dict(request.form, 'set__account', 'set__name' ,'set__email')
            to_md5_dict = get_dict(request.form, 'set__pwd')
            to_md5_list=to_md5_dict.values()
            to_md5_str=str(to_md5_list[0])

            set_pwd_md5 = hashlib.md5()# use hashlib.md5
            set_pwd_md5.update(to_md5_str) # to md5
            set_pwd = set_pwd_md5.hexdigest()#print 編碼後的結果至終端
            user_dict['set__pwd'] = set_pwd

            try:
                User.objects(id=request.form['objid']).update(**user_dict)
            except ValidationError as e:
                return redirect(url_for('admin.list',**e.errors))

        if action=='delete':
            try:
                User(id=request.form["objid"]).delete()

            except ValidationError as e:
                return redirect(url_for('admin.list',**e.errors))

        return redirect(url_for('admin.list'))


admin_view = ListView.as_view('list')
admin.add_url_rule('/admin/',
    view_func=admin_view, methods=['GET', 'POST'])

