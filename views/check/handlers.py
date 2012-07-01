# -*- coding: utf-8 -*-
from tipfy.app import Response
from main import DefaultHandler

import httplib, time, sys
from time import mktime
from copy import copy

from datetime import datetime

#Importing the models
from db.models import SiteMonitor, Log

from main import dbg

class CheckUPHandler(DefaultHandler):
    def get(self):
        sites = SiteMonitor.getAll()
        log = []
        for site in sites:
            if site.flagAtivo:
                result = self.checaSite(site.link, site.textCheck)
                log.append(result)
                
                save = Log(site_monitor = site.key(),
                           date_creation = datetime.now(),
                           status = result.get('status',False),
                           time_access = result.get('time_access'),
                           speed_access = result.get('speed_access'))
                save.put()
        
        
        
        
        
        return Response(log)
        
        
        
        


    def checaSite(self, url, textcheck):
        if url.startswith('https://'):
            location = url.replace('https://', '')
            use_ssl = True
        elif url.startswith('http://'):
            location = url.replace('http://', '')
            use_ssl = False
        else:
            location = url
            use_ssl = False
            
        if '/' in location:
            parts = location.split('/')
            host = parts[0]
            path = '/' + '/'.join(parts[1:])
        else:
            host = location
            path = '/'
    
        return self.run(host, path, textcheck, use_ssl)


    
    def run(self, host, path, textcheck, use_ssl=False):
        D = {}
        # select most accurate timer based on platform
        if sys.platform.startswith('win'):
            default_timer = time.clock
        else:
            default_timer = time.time
    
        start_run = default_timer()
        if use_ssl:
            conn = httplib.HTTPSConnection(host)
        else:
            conn = httplib.HTTPConnection(host)
            
        conn.request('GET', path)
        resp = conn.getresponse()
        data = copy(resp.read())
        
        if textcheck in data.decode( 'utf-8', 'ignore') :
            D['status'] = True
        else:
            D['status'] = False
        
        size = len(data)
        conn.close()     
        end_run = default_timer()
        
        #dbg()
        
        full_time = end_run - start_run
        #datetime.fromtimestamp(full_time)
        datetime.fromtimestamp(time.time())
        D['time_access'] = datetime.fromtimestamp(full_time).microsecond

        # Kb/s
        D['speed_access'] = int((size /1000.0)/full_time)
         
        
        return D
    

