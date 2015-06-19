# -*- coding: utf-8 -*-
from tipfy.app import Response
from tipfy.handler import RequestHandler
from google.appengine.ext import db

from db.models import Log
from datetime import datetime, timedelta

class DeleteEntryHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""

        hoje = datetime.now()
        start_date = hoje - timedelta(days=60)
        result = db.GqlQuery("SELECT __key__ FROM Log WHERE date_creation <= :1",start_date)

        count = result.count()
        db.delete(result)

        return Response('Limpesa do Banco realizada: itens removidos = %s' %(count))