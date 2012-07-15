# -*- coding: utf-8 -*-
from tipfyext.jinja2 import Jinja2Mixin
from main import DefaultHandler

from db.models import SiteMonitor,Log
from datetime import date, timedelta

from main import dbg

class HistoryGraphicHandler(DefaultHandler, Jinja2Mixin):
    def get(self):
        self.context['message'] = 'Historico / Graficos'
        
        self.context['resources'].css.append('start/jquery-ui-1.8.21.custom.css')
        for i in ['jscharts.js','ajax-grafic.js','jquery-ui-1.8.21.custom.min.js','jquery.ui.datepicker-pt-BR.js']:
            self.context['resources'].js.append(i)
        
        self.context['sites'] = SiteMonitor.getAll()
        
        startDate = date.today() - timedelta(days=30)
        self.context['start_date'] = startDate.strftime('%d/%m/%Y') 
        self.context['end_date'] = date.today().strftime('%d/%m/%Y') 
       
        return self.render_response('historygraphic.html', **self.context)
    
    
class GraphicAjaxHandler(DefaultHandler, Jinja2Mixin):
    def get(self): 
        param = self.request.args 
        
        if param.has_key('site') and\
           param.has_key('start_date') and param.has_key('end_date'):
            #dbg()
            site = param.get('site')
            start_date = param.get('start_date').split('/')
            end_date = param.get('end_date').split('/')
            
            result = Log.getLogGrafic(site,date(int(start_date[2]),int(start_date[1]),int(start_date[0])),
                                           date(int(end_date[2]),int(end_date[1]),int(end_date[0]))
                                     )
            
            L_time_access = []
            L_speed_access = []
            
            cont = 0
            for item in result:
                cont += 1
                L_speed_access.append([cont,item.speed_access])
                L_time_access.append([cont,item.time_access])
            
            
            self.context['resultSite'] = [tuple(L_time_access),tuple(L_speed_access)]

        
        
        else:
            pass

        return self.render_response('ajaxgraphic.html', **self.context)