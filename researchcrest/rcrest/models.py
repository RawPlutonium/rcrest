# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
emailvalidator = EmailValidator(message="invalid email")
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, validators=[emailvalidator])
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name +" "+ self.password +" "+ self.email
