# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.views import generic
from django.http import response
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from models import Member
from forms import LoginForm

# Create your views here.

class LoginView(generic.TemplateView):

    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        
        l_form = LoginForm(request.POST)

        if l_form.is_valid():
            email = l_form.cleaned_data['email']
            password = l_form.cleaned_data['password']
            try:
                member = Member.objects.get(email=email)
                if check_password(password, member.password):
                    auth.login(request, member)
                    ret = {
                        'code': 200,
                        'message': _('Login success.'),
                        'redirect': reverse('member_login')
                    }
                    return response.JsonResponse(ret)
                else:
                    ret = {
                        'code': 403,
                        'message': _('Password error.')
                    }
                    return response.JsonResponse(ret)
            except Member.DoesNotExist:
                ret = {
                    'code': 404,
                    'message': _('Username not exist.')
                }
                return response.JsonResponse(ret)
        else:
            context = {
                'errors': l_form.errors
            }
            return render(request, 'login.html', context)
