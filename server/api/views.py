from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Item, Category, Rank, AuditLog
from .serializers import CategorySerializer, ItemSerializer, AuditLogSerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SingleItemView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SingleItemRankView(APIView):

    def get(self, request, pk):
        rank = Rank.objects.first()

        try:
            item_rank = rank.data[pk]
            return Response({'guid': pk, 'rank': item_rank}, status=status.HTTP_200_OK)
        except (AttributeError, KeyError):
            raise Http404
    
    def put(self, request, pk):
        rank_obj = Rank.objects.first()
            
        if not rank_obj or not rank_obj.data.get(pk):
            raise Http404

        if not isinstance(request.data, dict):
            message = "Invalid data. Must be a dictionary."
            return Response({"non_field_errors": [message]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_rank = int(request.data.get('rank'))
        except (TypeError, ValueError):
            return Response({'detail': f'Rank must be a positive integer'}, status=status.HTTP_400_BAD_REQUEST)

        rank_obj.update_item(pk, new_rank)
        rank_obj.save()

        return Response({'guid': pk, 'rank': new_rank}, status=status.HTTP_200_OK)


class AuditLogView(ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
