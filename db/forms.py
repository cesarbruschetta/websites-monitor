# -*- coding: utf-8 -
from tipfyext.wtforms import Form, fields
from tipfyext.wtforms import validators

from db.models import SiteMonitor

class SiteMonitorForm(Form):
    
    name = fields.TextField(u'Nome do Site',
                            [validators.Required(message=u'O Campo não pode ficar vazio')])
    
    link = fields.TextField(u'Endereço do Site',
                            [validators.Required(message=u'O Campo não pode ficar vazio'),
                             validators.URL(message=u'Digite um site valido')])
    
    textCheck = fields.TextField(u'Texto de checagem do site',
                                 [validators.Required(message=u'O Campo não pode ficar vazio')])
    
    flagAtivo = fields.BooleanField(u'Site Ativo?',
                                    default=True)
    
