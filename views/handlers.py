# -*- coding: utf-8 -*-
from tipfy.app import Response,redirect
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
        context = {
            'message': 'Hello, World!',
            'data':SiteMonitor.getAll()
        }
        return self.render_response('views/list_sites.html', **context)


class ManageSiteMonitorHandler(DefaultHandler, Jinja2Mixin):
    
    def get(self):
        
        self.context['message'] = 'Hello, World!'
        if self.request.args.has_key('key'):
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
        dbg()
        #http://flask.pocoo.org/snippets/60/     
               
        if self.request.form.has_key('registre') and\
           self.request.args.has_key('key'):
            
            key =  self.request.args.get('key')
            obj = SiteMonitor.getByID(key)
            
            MyForm = model_form(SiteMonitor, SiteMonitorForm)
            form = MyForm(self.request.form, obj)
            
            if form.validate_on_submit():
                form.populate_obj(obj)
                obj.put()
                
                return redirect('/') 
        
        if self.request.form.has_key('registre'):    
            self.context['form'] = self.form #SiteMonitorForm()
            self.context['errors_loginform_add'] = ''
            
            # Validate the form.
            if self.form.validate():
                # Form is valid. Use the form data and redirect the user to the
                # final destination.
                #dbg()
                
                record = SiteMonitor(name = self.form.name.data,
                                     link = self.form.link.data,
                                     textCheck = self.form.textCheck.data,
                                     date_creation = datetime.now(),
                                     flagAtivo = self.form.flagAtivo.data)
            
                record.put()

                return redirect('/')
                
            
            # Since the form didn't validate, render it again using self.get().
            return self.render_response('views/manage_sites.html', **self.context)
        
    
    @cached_property
    def form(self):
        """We define a form as a cached property instantiated on first call.
        It is constructed passing the request object to populate it.
        """
        if self.request.form.has_key('registre'):
            return SiteMonitorForm(self.request)
 
    
    
    