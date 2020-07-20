from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORY_CHOICES=(
    ('Fashion','Fashion'),
    ('Toys','Toys'),
    ('Electronics','Electronics'),
    ("Home","Home")
)
class User(AbstractUser):
    pass


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    minimum = models.IntegerField(blank=False)
    # image = models.ImageField(upload_to='items', default = '../noimg.png')
    image = models.URLField()
    category = models.CharField(max_length=100, blank=True, choices=CATEGORY_CHOICES)

    is_active = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.name


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bid')
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return self.user


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.user
