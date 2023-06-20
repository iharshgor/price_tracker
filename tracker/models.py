from django.db import models


# Create your models here.
class Product(models.Model):
    link = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.link


class History(models.Model):
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.price
