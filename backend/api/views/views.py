from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from api.serializers.user_serializers import UserSerializer, RegistrationSerializer
from api.serializers.device_key_serializer import DeviceKeySerializer, DeviceKeyTransferSerializer
from api.serializers.organization_serializer import OrganizationSerializer
from django.contrib.auth import get_user_model
from api.models.device_key import DeviceKey
from api.models.organization import Organization

User = get_user_model()


class UserList(APIView):
    """
    List all users, or create a new user
    """

    def get(self, request, format=None):
        users = User.objects.all()

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


class DeviceKeyList(APIView):
    """
    List all device key, or create a new device key
    """

    def get(self, request, format=None):
        device_key = DeviceKey.objects.all()
        serializer = DeviceKeySerializer(device_key, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceKeySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceKeyDetail(APIView):
    """
    Read, update, or delete a device key
    """

    def get(self, request, pk, format=None):
        device_key = DeviceKey.objects.get(pk=pk)
        serializer = DeviceKeySerializer(device_key, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        device_key = DeviceKey.objects.get(pk=pk)
        serializer = DeviceKeySerializer(device_key, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        device_key = DeviceKey.objects.get(pk=pk)
        device_key.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceKeyTransfer(APIView):
    """
    Transfer device key from one organization to another
    """
    serializer_class = DeviceKeyTransferSerializer

    def post(self, request, format=None):
        """
        org_id -- organization to transfer to
        dev_eui -- dev_eui to trensfer
        """
        serializer = DeviceKeyTransferSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            org_id = serializer.data['org_id']
            dev_eui = serializer.data['dev_eui']
            try:
                device_key = DeviceKey.objects.get(dev_eui=dev_eui)
            except DeviceKey.DoesNotExist:
                raise serializers.ValidationError("Device key does not exist!")

            try:
                org = Organization.objects.get(pk= org_id)
            except Organization.DoesNotExist:
                raise serializers.ValidationError("Organzation does not exist!")

            if request.user.organizations.filter(pk=device_key.organization.pk).exists():
                device_key.organization = org
                device_key.save()
                serializer = DeviceKeySerializer(device_key)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise serializers.ValidationError("User is not allowed to transfer this key!")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationList(APIView):
    """
    List all organization, or create a new organization
    """

    def get(self, request, format=None):
        organization = Organization.objects.all()
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganizationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationDetail(APIView):
    """
    Read, update, or delete a organization
    """

    def get(self, request, pk, format=None):
        organization = Organization.objects.get(pk=pk)
        serializer = OrganizationSerializer(organization, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        organization = Organization.objects.get(pk=pk)
        serializer = OrganizationSerializer(organization, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        organization = Organization.objects.get(pk=pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)