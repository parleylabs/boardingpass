from rest_framework import serializers
from api.models.device_key import DeviceKey


class DeviceKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceKey
        fields = '__all__'
