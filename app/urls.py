from django.urls import path

from . import views


urlpatterns = [
    path('category/', views.category_list_create_api_view, name="category"),
    path('product/', views.product_list_create_api_view, name="product")
]
