from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.authentication.permissions import can_create_user_in_org, can_create_superuser
from api.serializers.organization_serializer import OrganizationSerializer, OrganizationPostSerializer
from api.models.organization import Organization
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'username', 'organizations', 'is_staff', 'is_superuser']


class UserEditSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), many=True)

    def create(self, validated_data):
        organizations = validated_data.pop('organizations')
        user = User.objects.create_user(**validated_data)
        user.organizations.set(organizations)
        return user

    def update(self, instance, validated_data):
        organizations = validated_data.pop('organizations')
        instance.organizations.set(organizations)
        fields = ['first_name', 'last_name', 'email', 'username', 'is_staff', 'is_superuser']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'organizations', 'is_staff', 'is_superuser']


class RegistrationSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), many=True)
    password = serializers.CharField(write_only=True)

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

        for org in data['organizations']:
            if not can_create_user_in_org(user, org ):
                raise serializers.ValidationError("You do not have permissions to create user within this org: {}".format(org))

        return data

    def create(self, validated_data):
        organizations = validated_data.pop('organizations')
        user = User.objects.create_user(**validated_data)
        user.organizations.set(organizations)
        return user

    class Meta:
        model = User
        fields = ['first_name', 'password', 'last_name', 'email', 'username', 'organizations', 'is_staff', 'is_superuser']
