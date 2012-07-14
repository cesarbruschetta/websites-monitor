# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    #Login User
    Rule('/logout', endpoint='auth/logout', handler='handlers.Logout'),         
         
    Rule('/', name='hello-world', handler='views.home.handlers.HomePageHandler'),
    # Gerencias Sites
    Rule('/sites', name='Gerenciar Sites', handler='views.manage.handlers.SiteMonitorHandler'),
    Rule('/sites/manage-sites', name='Gerenciar Sites', handler='views.manage.handlers.ManageSiteMonitorHandler'),
    
    # Historicos
    Rule('/history', name='Historico / Graficos', handler='views.history.handlers.HistoryGraphicHandler'),
    
    # Checagem pelo Cron
    Rule('/checkup', name='Checagem dos sites', handler='views.check.handlers.CheckUPHandler'),
]
