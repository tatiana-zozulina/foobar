from django.db import models

class MenuItem(models.Model):
	name = models.CharField(max_length=40)
	link = models.CharField(max_length=600)
	