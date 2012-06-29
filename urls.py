# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='hello-world', handler='hello_world.handlers.HelloWorldHandler'),
    # Gerencias Sites
    Rule('/sites', name='Gerenciar Sites', handler='views.handlers.SiteMonitorHandler'),
    Rule('/manage-sites', name='Gerenciar Sites', handler='views.handlers.ManageSiteMonitorHandler'),
    
    
]
