from django.db import models

# Create your models here.
from django.db import models


class MenuItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=500)
    item_picture_url = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now=True)