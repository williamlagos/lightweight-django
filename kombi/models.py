""" Models for application project """

from django.db import models

class Delivery(models.Model):
    """ Main delivery model """
    freighter = models.IntegerField(default=models.NOT_PROVIDED)
    departure = models.CharField(max_length=256)
    arrival = models.CharField(max_length=256)
    deadline = models.DateTimeField(auto_now=True)
    volume = models.FloatField(default=models.NOT_PROVIDED)
    weight = models.FloatField(default=models.NOT_PROVIDED)
    image = models.ImageField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True)
    def __unicode__(self):
        pass
    def __str__(self):
        return self.title
