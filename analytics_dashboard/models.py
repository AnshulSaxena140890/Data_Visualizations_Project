# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models
class AdvData(models.Model):

	advertiser_name = models.CharField(max_length=100)
	publisher_name = models.CharField(max_length=100)
	impression = models.PositiveIntegerField(default=0)
	click = models.PositiveIntegerField(default=0)
	install = models.PositiveIntegerField(default=0)
	purchase = models.PositiveIntegerField(default=0)
	os = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	device_brand = models.CharField(max_length=100)


#Code to import data from CSV to models (Done in Python Terminal) :-

# >>> import csv
# >>> import os
# >>> from analytics_dashboard.models import AdvData

# >>> path = "/home/anshul/Project"
# >>> os.chdir(path)
# >>> with open('assignment_data.csv') as csvfile:
# ...      reader = csv.DictReader(csvfile)
# ...      for rows in reader:
# ...               p = AdvData(advertiser_name=rows['advertiserName'],publisher_name=rows['publisherName'],impression=rows['impression'],click=rows['click'],install=rows['install'],purchase=rows['purchase'],os=rows['os'],city=rows['city'],device_brand=rows['deviceBrand'])
# ...               p.save()
