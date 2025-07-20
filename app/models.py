from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')
    condition = models.CharField(max_length=100)
    year = models.DateField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/images')
    def __str__(self):
        return self.name
