# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext as _

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emaiphonel, username, phone, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            username=username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        (0, _('unset')),
        (1, _('male')),
        (2, _('female'))
    )

    username = models.CharField(
        max_length=50, unique=True, verbose_name=_('username'))
    password = models.CharField(max_length=200, verbose_name=_('password'))
    email = models.EmailField(null=True, blank=True,
                              unique=True, verbose_name=_('Email'))
    phone = models.CharField(max_length=20, null=True,
                             blank=True, unique=True, verbose_name=_('phone'))
    gender = models.SmallIntegerField(
        default=0, null=True, choices=GENDER_CHOICES, verbose_name=_('gender'))
    real_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_('real name'))
    birth_of_date = models.DateField(
        null=True, verbose_name=_('birth of date'))
    is_superuser = models.BooleanField(
        default=False, verbose_name=_('whether super user or not'))
    is_staff = models.BooleanField(
        default=False, verbose_name=_('whether enter backend or not'))
    last_login = models.DateTimeField(
        null=True, verbose_name=_('last login datetime'))
    create = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create datetime'))
    modify = models.DateTimeField(
        auto_now=True, verbose_name=_('modify datetime'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    class Meta:
        db_table = 'member'
