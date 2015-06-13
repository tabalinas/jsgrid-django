from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    address = models.CharField(max_length=256)
    married = models.BooleanField()

    def __str__(self):
        return self.name