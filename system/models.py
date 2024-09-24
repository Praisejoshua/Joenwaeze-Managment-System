from django.db import models

# Create your models here.
class Managment(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    seller_name = models.CharField(max_length=200, blank=False)
    Weight = models.CharField(max_length=150, blank=False)
    amount = models.CharField(max_length=100, blank = False)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.seller_name