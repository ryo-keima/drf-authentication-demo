from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

    class Meta:
        model = User
        fields = "__all__"
