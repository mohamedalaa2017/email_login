from . import views


from django.urls import path
# from .views import RegisterView 

# from rest_auth.views import PasswordResetConfirmView
# LoginView

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
    # path('login/', views.CustomObtainAuthToken.as_view(), name='login'),


    # path("guest", views.GuestListView.as_view()),
]
