from django.urls import path

from crm.internal.products import views

urlpatterns = [
    path('products', views.ProductsGetCreate.as_view()),
    path('products/<str:id>', views.ProductGetUpdateDelete.as_view()),
]
