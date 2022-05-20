from rest_framework import generics
from .serealizers import ProductSerializer
from .models import Product
from django.http import HttpResponse, JsonResponse


class Index(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


def single_product(request, index):
    serealized = ProductSerializer().to_representation(Product.objects.get(id=index))
    return JsonResponse(serealized)

