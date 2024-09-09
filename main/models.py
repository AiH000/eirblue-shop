from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()

    @property
    def is_available(self):
        return True if self.stock >= 1 else False