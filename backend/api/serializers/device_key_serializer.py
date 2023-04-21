from rest_framework import serializers
from api.models.device_key import DeviceKey


class DeviceKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceKey
        fields = '__all__'


class DeviceKeyTransferSerializer(serializers.Serializer):
    org_id = serializers.IntegerField()
    dev_eui = serializers.CharField(max_length=75)
