# -*- coding: utf-8 -*-
from main import DefaultHandler
from tipfy.auth.google import GoogleMixin


from main import dbg
   
class Logout(DefaultHandler):
    def get(self, **kwargs):
        self.auth.logout()
        return self.redirect(self.redirect_path())

class GoogleAuthHandler(DefaultHandler, GoogleMixin):
    def get(self):
        url = self.redirect_path()

        if self.auth.session:
            # User is already signed in, so redirect back.
            return self.redirect(url)

        self.session['_continue'] = url

        if self.request.args.get('openid.mode', None):
            return self.get_authenticated_user(self._on_auth)

        return self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            self.abort(403)

        auth_id = 'google|%s' % user.pop('email', '')
        self.auth.login_with_auth_id(auth_id, remember=True)
        return self._on_auth_redirect()

