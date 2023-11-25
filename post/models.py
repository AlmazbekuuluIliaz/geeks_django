from django.db import models

# Create your models here.

#ORM - Object Relational Mapper

class Post(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} {self.title}'

class Product(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'
