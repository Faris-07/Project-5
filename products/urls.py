from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductsView, name='products'),
    path('<int:product_id>/', views.ProductDetail, name='product_detail'),
    path('add/', views.AddProduct, name='add_product'),
    path('edit/<int:product_id>/', views.EditProduct, name='edit_product'),
]
