# -*- coding: utf-8 -*-
from main import DefaultHandler
from tipfy.app import redirect
from google.appengine.api import users

class Logout(DefaultHandler):
    def get(self):
        return redirect(users.create_logout_url('/'))
