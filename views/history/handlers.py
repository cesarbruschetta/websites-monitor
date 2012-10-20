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
        for i in ['ajax-grafic.js','jquery-ui-1.8.21.custom.min.js','jquery.ui.datepicker-pt-BR.js']:
            self.context['resources'].js.append(i)
            
        #JSCharts
        #self.context['resources'].css.append('jscharts.js')
        
        #Outro grafico
        for i in ['highcharts.js','modules/exporting.js']:
            self.context['resources'].js.append(i)
        
        self.context['sites'] = SiteMonitor.getAll()
        
        startDate = date.today() - timedelta(days=1)
        self.context['start_date'] = startDate.strftime('%d/%m/%Y') 
        self.context['end_date'] = date.today().strftime('%d/%m/%Y') 
       
        return self.render_response('historygraphic.html', **self.context)
    
    
class GraphicAjaxHandler(DefaultHandler, Jinja2Mixin):
    
    #quebrando tudo
    def quebrador(self, lista, partes):
        return list(lista[ parte*len(lista)/partes:(parte+1)*len(lista)/partes ] for parte in range(partes))
    
    def GeraMedia(self, lista):
        tmp = self.quebrador(lista, 20)
        
        L = []
        for item in tmp:
            D = {}
            D['axisX'] = item[0].get('axisX')
            
            soma = 0
            cont = 0
            for i in item:
                cont += 1
                soma += i.get('axisY',0)
            
            D['axisY'] = soma/cont
             
            L.append(D)
        
        return L 
    
    def get(self): 
        param = self.request.args 
        
        if param.has_key('site') and\
           param.has_key('start_date') and param.has_key('end_date'):
            
            site = param.get('site')
            start_date = param.get('start_date').split('/')
            end_date = param.get('end_date').split('/')
            
            result = Log.getLogGrafic(site,date(int(start_date[2]),int(start_date[1]),int(start_date[0])),
                                           date(int(end_date[2]),int(end_date[1]),int(end_date[0])+1)
                                     )
                
            L_time_access = []
            L_speed_access = []
            status_OK = 0
            status_Failed = 0
            
            for item in result:
                S = {}
                T = {}
                T['axisX'] = S['axisX'] = item.date_creation.strftime('%d-%m %H:%M')
                
                T['axisY'] = item.time_access
                S['axisY'] = item.speed_access
                
                L_speed_access.append(S)
                L_time_access.append(T)
                
                if item.status:
                    status_OK += 1
                else:
                    status_Failed += 1 
            
            
            L_status = [{'axisX':'OK',
                         'axisY':status_OK},
                        {'axisX':'Down',
                         'axisY':status_Failed}]
            
            if len(L_time_access) > 20:
                L_time_access = self.GeraMedia(L_time_access)
                
            if len(L_speed_access) > 20:
                L_speed_access = self.GeraMedia(L_speed_access)
                
            self.context['resultSite'] = [{'id':'time_access',
                                           'name':"Tempo de Acesso",
                                           'nameX':"Periodo (dias)",
                                           'nameY':'Tempo (seg)',
                                           'type':'line',
                                           'data':L_time_access},
                                          {'id':'speed_access',
                                           'name':'Velocidade de acesso',
                                           'nameX':"Periodo (dias)",
                                           'nameY':'Velocidade (KB/s)',
                                           'type':'line',
                                           'data':L_speed_access},
                                          {'id':'status',
                                           'name':'Historico de Status',
                                           'nameX':"Status",
                                           'nameY':'Quantidate',
                                           'type':'bar',
                                           'data':L_status}
                                          ]
        
        else:
             self.context['resultSite'] = []

        return self.render_response('ajaxgraphic.html', **self.context)