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
        Validate permissions on superuser and staff
        1. superuser can create other super users and staff in any organizations
        2. staff can create other staff and general user in only their organization
        3. general users cannot create users
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
