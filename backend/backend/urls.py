from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from django.urls import path, include
# from rest_framework import routers
# from recipes import views
#
# router = routers.DefaultRouter()
# router.register(r'recipes', views.RecipeView, 'recipe')
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]

from django.urls import path
from recipes import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.recipeOverview, name="recipe_overview"),
    path('recipe_list/', views.recipeList),
    path('recipe_list/<str:pk>/', views.recipeDetail, name = "recipe_detail"),
    path('categories', views.categoryList, name = "categories"),
    path('categories/<str:pk>/', views.recipeByCategory, name = "recipe_filtered"),
    path('categories/name/<str:pk>/', views.categoryName, name = "category_name"),
    path('users/', views.userList, name = "users"),
    path('users/<str:pk>/', views.userDetail, name = "user"),
    path('recipe/<str:pk>/user/', views.postAuthor, name = "author"),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)