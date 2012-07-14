# -*- coding: utf-8 -*-
"""App configuration."""
#Constants
website_title = 'Monitoramento de Sites by AppEngine Google'

send_mail = 'cesaraugusto@liberiun.com'
send_to = 'cesarbruschetta@hotmail.com'

config = {}

config['tipfy.sessions'] = {
       'secret_key': '581a6ac0061a07fd9c01f79b16d8cebf',
   }

config['tipfy.ext.i18n'] = {
    # Change default values from the internalization module.
    'locale':   'pt_BR',
    'timezone': 'America/Sao_Paulo',
}


# Configiração do fuso horario global
# America/Sao_Paulo
config['time_zone'] = {'UTF': -3}


# Configurations for the 'tipfy' module.
config['tipfy'] = {
    'auth_store_class': 'tipfy.auth.MultiAuthStore',
}

config['tipfyext.jinja2'] = {
    'environment_args': {
        'autoescape': True,
        'extensions': [
            'jinja2.ext.autoescape',
            'jinja2.ext.i18n',
            'jinja2.ext.with_'
        ],
    },
}