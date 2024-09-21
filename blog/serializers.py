from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email')
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
