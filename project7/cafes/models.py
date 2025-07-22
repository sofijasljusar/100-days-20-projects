from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=250, unique=True)
    map_url = models.URLField(max_length=500)
    img_url = models.URLField(max_length=500)
    location = models.CharField(max_length=250)
    seats = models.CharField(max_length=250)
    has_toilet = models.BooleanField()
    has_wifi = models.BooleanField()
    has_sockets = models.BooleanField()
    can_take_calls = models.BooleanField()
    coffee_price = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
