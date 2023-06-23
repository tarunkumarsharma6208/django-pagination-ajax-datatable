from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name