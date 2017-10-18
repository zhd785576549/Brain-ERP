from django import forms
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):

    email_error_messages = {
        'required': _('Email is required!'),
        'invalid': _('Email is invalid!')
    }

    passowrd_error_message = {
        'required': _('Password is required!'),
        'max_length': _('Password max length is 20!'),
        'min_length': _('Password min length is 6')
    }

    email = forms.EmailField(
        required=True, error_messages=email_error_messages)
    passowrd = forms.CharField(
        max_length=20, min_length=6, error_messages=passowrd_error_message)
