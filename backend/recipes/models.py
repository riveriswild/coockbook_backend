from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass



class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=500, null=True, blank=True)
    recipeCategory = models.ManyToManyField(Category, verbose_name='Категория')
    text = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


# Create your models here.
