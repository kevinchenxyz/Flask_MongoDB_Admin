#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request, redirect
from flask.views import MethodView
from flask.ext.login import (login_required, login_user, logout_user,
                            current_user)

from model import User
from wtforms import ValidationError
from forms import LoginForm

users  = Blueprint('users', __name__, template_folder='templates')

class LoginView(MethodView):

    def get(self):
        if current_user.is_authenticated():
            return redirect(url_for('admin.list'))
        else:
            form = LoginForm()
            return render_template('login.html',form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = form._get_user()
            login_user(user)
            return redirect(url_for('admin.list'))
        return render_template('login.html', form=form)


class LogoutView(MethodView):

    @login_required
    def get(self):
        logout_user()
        return redirect(url_for('users.login'))


users.add_url_rule('/', view_func=LoginView.as_view('login'))
users.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))

