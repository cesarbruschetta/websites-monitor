# -*- coding: utf-8 -
from google.appengine.api import memcache
from google.appengine.ext import db

from main import dbg

class SiteMonitor(db.Model):
    """Table of the database used to save the data 
        of the site of monitoring """

    name = db.StringProperty(required=True)
    link = db.LinkProperty(required=True)
    textCheck = db.StringProperty(required=True)
    date_creation = db.DateTimeProperty(auto_now_add=True)
    flagAtivo = db.BooleanProperty(default=True)
    
    @classmethod
    def getAll(self):
        return SiteMonitor.all()
    
    @classmethod
    def getByID(self,id):
        return db.GqlQuery("SELECT * FROM SiteMonitor WHERE __key__ = :1 ", db.Key(id)).get()
    
class Log(db.Model):
    """Table of the database used to save the data 
        of log of the sites monitoring """
  
    site_monitor = db.ReferenceProperty(SiteMonitor, collection_name = 'site_log')
    date_creation = db.DateTimeProperty(auto_now_add=True)
    status = db.BooleanProperty()
    time_access = db.FloatProperty()
    speed_access = db.FloatProperty()
    
    
    