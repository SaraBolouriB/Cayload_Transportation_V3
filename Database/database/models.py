from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models


# MODELS -----------------------------------------------------------------------
class Site(models.Model):
    siteName = models.CharField(default=None, max_length=50, unique=True, null=True, blank=True)
    adminUsername = models.CharField(default='admin', max_length=50)
    adminPassword = models.CharField(default='admin', max_length=50)

class Service(models.Model):
    name = models.CharField(default=None, max_length=50, unique=True, null=True, blank=True)
    url = models.CharField(default=None, max_length=200)
    params = models.CharField(default=None, max_length=200, null=True, blank=True)
    data = models.CharField(default=None, max_length=1000)
    created_on = models.CharField(default=None, max_length=200)
    user_info = models.CharField(default=None, max_length=200)
    contract_info = models.CharField(default=None, max_length=200)

class Blockchian(models.Model):
    site_id =  models.CharField(default=None, max_length=200)
    url = models.CharField(default=None, max_length=200)
    

class Login(models.Model):
    url = models.CharField(default=None, max_length=200, unique=True, null=True, blank=True)
    data = models.CharField(default=None, max_length=200)

# ------------------------------------------------------------------------------
# CONNECTION -------------------------------------------------------------------
class SiteService(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

class SiteBlockhain(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE, unique=True, null=True, blank=True)
    blockchain = models.ForeignKey('blockchian', on_delete=models.CASCADE)

class SiteLogin(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE, unique=True, null=True, blank=True)
    login = models.ForeignKey('Login', on_delete=models.CASCADE)
# -------------------------------------------------------------------------------
