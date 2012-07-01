# -*- coding: utf-8 -*-
"""WSGI app setup."""
import os
import sys


# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
lib_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib')
if lib_path not in sys.path:
    #sys.setdefaultencoding("utf-8")
    sys.path[0:0] = [
        lib_path,
        os.path.join(lib_path, 'dist'),
        os.path.join(lib_path, 'dist.zip'),
    ]
    

from tipfy.app import App
from config import *
from urls import rules
from tipfy.handler import RequestHandler

#Importing some utilities
from utils import Resources 
from config import website_title

def enable_appstats(app):
    """Enables appstats middleware."""
    from google.appengine.ext.appstats.recording import \
        appstats_wsgi_middleware
    app.dispatch = appstats_wsgi_middleware(app.dispatch)

def enable_jinja2_debugging():
    """Enables blacklisted modules that help Jinja2 debugging."""
    if not debug:
        return
    from google.appengine.tools.dev_appserver import HardenedModulesHook
    HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']

def dbg():
    """ Enter pdb in App Engine
        Renable system streams for it.
    """
    import pdb
    import sys
    pdb.Pdb(stdin=getattr(sys,'__stdin__'),stdout=getattr(sys,'__stderr__')).set_trace(sys._getframe().f_back)


# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = App(rules=rules, config=config, debug=debug)
enable_appstats(app)
enable_jinja2_debugging()


class DefaultHandler(RequestHandler):
    """
    Default class that provides resources and user information handling.
    """
    resources = None
    user_info = None
    template_vars = {}
    
    def __init__(self, request, app=None):
        
        super(DefaultHandler, self).__init__(request)
        self.resources = Resources()
        self.template_vars = {'resources':self.resources,
                              'page_title':website_title,
                              }
        self.context = self.template_vars


def main():
    app.run()

if __name__ == '__main__':
    main()
