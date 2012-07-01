# -*- coding: utf-8 -*-
from tipfy.app import redirect
from wtforms.ext.appengine.db import model_form
from tipfyext.jinja2 import Jinja2Mixin, cached_property
from main import DefaultHandler

from datetime import datetime

#Importing the forms
from db.forms import SiteMonitorForm

#Importing the models
from db.models import SiteMonitor

from main import dbg

class SiteMonitorHandler(DefaultHandler, Jinja2Mixin):
    def get(self):
        self.context['data'] = SiteMonitor.getAll()
        return self.render_response('views/list_sites.html', **self.context)

class ManageSiteMonitorHandler(DefaultHandler, Jinja2Mixin):
    def get(self):
        
        self.context['message'] = 'Hello, World!'
        if self.request.args.has_key('key') and\
           self.request.args.has_key('remove'):
            
            key =  self.request.args.get('key')
            obj = SiteMonitor.getByID(key)
            obj.delete()
            
            return redirect('/sites')
        
        elif self.request.args.has_key('key'):
            key =  self.request.args.get('key')
            obj = SiteMonitor.getByID(key)
            
            MyForm = model_form(SiteMonitor, SiteMonitorForm)
            form = MyForm(self.request.form, obj)

            self.context['form'] = form
            
        else:
            self.context['form'] = SiteMonitorForm()
        
        return self.render_response('views/manage_sites.html', **self.context)
    
    
    def post(self, **kwargs):
        """To process a form, we validate it, authenticate the User 
        and pass the form instance to the template.
        """
        #http://flask.pocoo.org/snippets/60/     
               
        if self.request.form.has_key('registre') and\
           self.request.args.has_key('key'):
            
            key =  self.request.args.get('key')
            obj = SiteMonitor.getByID(key)
            
            # Validate the form.
            if self.form.validate():
            
                obj.name = self.form.name.data
                obj.link = self.form.link.data
                obj.textCheck = self.form.textCheck.data
                obj.date_creation = datetime.now()
                obj.flagAtivo = self.form.flagAtivo.data
              
                obj.put()
                return redirect('/sites') 
        
        if self.request.form.has_key('registre'):    
            self.context['form'] = self.form #SiteMonitorForm()
            self.context['errors_loginform_add'] = ''
            
            # Validate the form.
            if self.form.validate():
                # Form is valid. Use the form data and redirect the user to the
                # final destination.
                
                record = SiteMonitor(name = self.form.name.data,
                                     link = self.form.link.data,
                                     textCheck = self.form.textCheck.data,
                                     date_creation = datetime.now(),
                                     flagAtivo = self.form.flagAtivo.data)
            
                record.put()
                return redirect('/sites')
            
            # Since the form didn't validate, render it again using self.get().
            return self.render_response('views/manage_sites.html', **self.context)
        
    
    @cached_property
    def form(self):
        """We define a form as a cached property instantiated on first call.
        It is constructed passing the request object to populate it.
        """
        if self.request.form.has_key('registre'):
            return SiteMonitorForm(self.request)
 
