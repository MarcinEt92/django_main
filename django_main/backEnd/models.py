from django.db import models


# Create your models here.
from django.urls import reverse


class Order(models.Model):
    buns = models.IntegerField(default=0)
    donuts = models.IntegerField(default=0)


class List(models.Model):
    def get_absolute_url(self):
        return reverse("specific_list", args=[self.id])


class Item(models.Model):
    text = models.TextField(default="", blank=False, unique=True)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

