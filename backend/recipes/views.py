from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Recipe, Category
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def recipeOverview(request):
    api_urls = {
        'List': '/recipe_list/',
        'Detail View': '/recipe_list/<str:pk>',
        'Category List': '/categories/',
        'Category': '/categories/name/<str:pk>',
        'Recipe by Category': 'categories/<str:pk>',
        'Users': 'users/',
        'User': 'users/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])

def recipeList(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])

def recipeDetail(request, pk):
    recipies = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipies, many=False)
    return Response(serializer.data)

@api_view(['GET'])

def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def categoryName(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['GET'])

def recipeByCategory(request, pk):
    category_pk = pk
    recipies = Recipe.objects.filter(recipeCategory__pk=category_pk)
    serializer = RecipeSerializer(recipies, many=True)
    return Response(serializer.data)


@api_view(['GET'])

def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def userDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['GET'])

def postAuthor(request, pk):
    recipe = Recipe.objects.get(id=pk)
    author = recipe.author
    serializer = UserSerializer(author, many=False)
    return Response(serializer.data)

