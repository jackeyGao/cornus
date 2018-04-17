# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from web.models import Profile

class ProfileMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_anonymous:
            if not request.user.is_active:
                return HttpResponse('not active')
 
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
