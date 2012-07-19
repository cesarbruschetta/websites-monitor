# -*- coding: utf-8 -*-
from tipfyext.jinja2 import Jinja2Mixin
from main import DefaultHandler

from tipfy.app import Response
from tipfy.handler import RequestHandler

from db.models import SiteMonitor

class HelloWorldHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""
        return Response('Hello, World!')

class HomePageHandler(DefaultHandler, Jinja2Mixin):
    def get(self):
        self.context['message'] = 'Monitoramento de Sites'
        self.context['sites'] = SiteMonitor.getAll()
       
        return self.render_response('homepage.html', **self.context)