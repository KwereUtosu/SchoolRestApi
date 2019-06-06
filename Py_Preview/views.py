from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import School
from .serializer import SchoolSerializer

# Create your views here.

class AllSchools(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SchoolView(APIView):

    def get(self, request, pk, format=None):
        try:
            school = School.objects.dates(pk=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        school = School.objects.dates(pk=pk)
        school.delete()
        return Response(status=status.HTTP_200_OK)
