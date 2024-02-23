from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Autho(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)