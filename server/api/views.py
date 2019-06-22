from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Item, Category
from .serializers import CategorySerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
