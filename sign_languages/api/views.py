from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model




# class UserLoginAPIView(APIView):
#     http_method_names = ['post']
#     permission_classes = [AllowAny]
    
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

# User = get_user_model()

# class UserRegistrationAPIView(APIView):
#     http_method_names = ['post']
#     permission_classes = [AllowAny]
    
#     def post(self, request, *args, **kwargs):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(using='create_user_without_username')  # Use the custom manager
#             email = serializer.validated_data.get('email')
#             user = User.objects.get(email=email)

#             # Create a token for the user
#             token, created = Token.objects.get_or_create(user=user)


#             return Response({'token': token.key})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginAPIView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

User = get_user_model()

class UserRegistrationAPIView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Use the default manager for user creation
            email = serializer.validated_data.get('email')
            user = User.objects.get(email=email)

            # Create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
