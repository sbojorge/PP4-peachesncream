from django.db import models


class Grocery(models.Model):
    name = models.CharField(max_length=100, default='My grocery list')
    item = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
