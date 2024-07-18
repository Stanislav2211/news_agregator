from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BBC, HackerNews
from .serializers import BbcSerializer, HackerNewsSerializer

class BbcNewsView(APIView):
    def get(self, request):
        queryset = BBC.objects.all()
        serializer = BbcSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BbcNewsDetailView(APIView):
    def get(self, request, pk):
        queryset = BBC.objects.get(pk=pk)
        serializer = BbcSerializer(queryset)
        return Response(serializer.data)

class HackerNewsView(APIView):
    def get(self, request):
        queryset = HackerNews.objects.all()
        serializer = HackerNewsSerializer(queryset, many=True)
        return Response(serializer.data)
    
class HackerNewsDetailView(APIView):
    def get(self, request, pk):
        queryset = HackerNews.objects.get(pk=pk)
        serializer = HackerNewsSerializer(queryset)
        return Response(serializer.data)