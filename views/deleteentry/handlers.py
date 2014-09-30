# -*- coding: utf-8 -*-
from tipfy.app import Response
from tipfy.handler import RequestHandler
from google.appengine.ext import db

from db.models import Log

class DeleteEntryHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""



        query = Log.all(keys_only=True)
        entries =query.fetch(100)
        db.delete(entries)
        # This could bulk delete 1000 entities a time



        return Response('Deletado 100 Dados')

