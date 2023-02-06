from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class hello(APIView):
    
    def get(self, request):
        return Response({"data": "Hello world"})