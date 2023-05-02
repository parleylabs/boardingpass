from rest_framework import serializers
from api.models.organization import Organization
from api.serializers.device_key_serializer import DeviceKeySerializer


class OrganizationSerializer(serializers.ModelSerializer):
    device_keys = DeviceKeySerializer(
        source='devicekey_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Organization
        fields = ['pk', 'name', 'device_keys']


class OrganizationPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['pk']