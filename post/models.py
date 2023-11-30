from django.db import models

# Create your models here.

#ORM - Object Relational Mapper

class HashTag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Post(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtag = models.ManyToManyField(
        HashTag,
        blank=True,
        related_name='posts'
    )
    def __str__(self) -> str:
        return f'{self.id} {self.title}'

class Product(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.title}'

class Comment(models.Model):
    post = models.ForeignKey(
        'post.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    text = models.TextField()
    release = models.DateField(auto_now_add=True)
