from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from yaml import serialize

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.date})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance =Women.odjects.get(pk=pk)
        except:
            return Response({"error":"Objects dose not exists"})

        serializer = WomenSerializer(data=request.date, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})
