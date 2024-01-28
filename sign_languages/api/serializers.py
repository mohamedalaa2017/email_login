from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if user and user.is_active:
            data['user'] = user
        else:
            raise serializers.ValidationError("Incorrect email or password")

        return data
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
    def save(self, *args, **kwargs):
        # Do not save the username field
        self.username = None
        super().save(*args, **kwargs)
