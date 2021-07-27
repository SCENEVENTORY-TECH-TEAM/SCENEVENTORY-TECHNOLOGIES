from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class UserInfoAPIView(APIView):
    
    def get(self, request):
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoDetails(APIView):
    def get_obeject(self, id):
        try:
            return UserInfo.objects.get(id=id)

        except UserInfo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user = self.get_obeject(id)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_obeject(id)
        serializer = UserInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        user = self.get_obeject(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
