# -*- coding: utf-8 -*-
from tipfyext.jinja2 import Jinja2Mixin
from main import DefaultHandler

class HistoryGraphicHandler(DefaultHandler, Jinja2Mixin):
    def get(self):
        self.context['message'] = 'Historico / Graficos'
       
        return self.render_response('historygraphic.html', **self.context)