from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('<int:index>/', views.single_product),
    path('create/', views.CreateProduct.as_view())
]
