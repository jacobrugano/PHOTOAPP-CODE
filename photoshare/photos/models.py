from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    imagetitle = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.description


    