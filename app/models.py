from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    year = models.DateField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/images')
    def __str__(self):
        return self.name
