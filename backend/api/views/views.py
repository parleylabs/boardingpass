from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.user_serializers import UserSerializer, RegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserList(APIView):
    """
    List all users, or create a new user
    """

    def get(self, request, format=None):
        if request.user.is_superuser:
            users = User.objects.all()
        else:
            users = User.objects.filter(organization=request.user.organization)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetail(APIView):
    """
    Read, update, or delete a user
    """

    def get(self, request, pk, format=None):
        user = User.objects.get(email=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(email=pk)
        serializer = UserSerializer(user, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(email=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)