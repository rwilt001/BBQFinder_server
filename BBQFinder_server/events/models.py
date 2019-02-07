from django.db import models
from .. import menu_items

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField('event date')
    location = models.CharField(max_length=200)
    exact_loc_lat = models.DecimalField('location_lat', decimal_places=4)
    exact_loc_lon = models.DecimalField('location_lon', decimal_places=4)
    menu_items = models.ManyToManyField(menu_items)