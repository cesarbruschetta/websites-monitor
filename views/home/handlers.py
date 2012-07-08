# -*- coding: utf-8 -*-
from tipfyext.jinja2 import Jinja2Mixin
from main import DefaultHandler

from tipfy.auth import (login_required, user_required)

#class HelloWorldHandler(RequestHandler):
#    def get(self):
#        """Simply returns a Response object with an enigmatic salutation."""
#        return Response('Hello, World!')

class HomePageHandler(DefaultHandler, Jinja2Mixin):
    #@user_required
    def get(self):
        self.context['message'] = 'Monitoramento de Sites'
        #users.create_logout_url("/")
       
        return self.render_response('homepage.html', **self.context)