# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=250, unique=True)
    map_url = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    has_sockets = models.BooleanField()
    has_toilet = models.BooleanField()
    has_wifi = models.BooleanField()
    can_take_calls = models.BooleanField()
    seats = models.CharField(max_length=250, blank=True, null=True)
    coffee_price = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False  # connecting to existing db (still read/write without managing structure)
        db_table = 'cafe'

    def __str__(self):
        return self.name
