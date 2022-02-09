from django.contrib import admin
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at')

#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title')

# Register your models here.

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)