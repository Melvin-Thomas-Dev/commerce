from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(balnk=False)
    minimum = models.IntegerField(blank=False)


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid')
    amount = models.IntegerField(blank=False)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False)
