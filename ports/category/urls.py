from django.urls import path
from rest_framework import routers

from ports.category import views

router = routers.DefaultRouter()
router.register('category', views.CategoryAPIView, basename='category')
router.register('autocomplete/category', views.CategoryAutocompleteView, basename='autocomplete_category')


urlpatterns = [
    path('<slug:cat>/', views.category, name='category'),
]
