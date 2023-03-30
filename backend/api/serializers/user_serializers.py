from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.authentication.permissions import can_create_user_in_org, can_create_superuser
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'organization', 'is_staff', 'is_superuser']


class RegistrationSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        user = self.context.get("request").user
        if data['is_superuser'] and not can_create_superuser(user):
            raise serializers.ValidationError("You do not have permissions to create superuser")

        if not can_create_user_in_org(user, data['organization']):
            raise serializers.ValidationError("You do not have permissions to create user within this org.")

        return data

    class Meta:
        model = User
        fields = '__all__'
