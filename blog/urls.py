
from django.urls import path
from .views import post_list
from . import views  # Import the views
from .views import UserRegistrationView, ObtainAuthTokenView

urlpatterns = [
    path('', post_list, name='post_list'),  # Redirects to the post_list view
    path('posts/', post_list, name='post_list'),  # Handles /blog/posts/
    path('signup/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', ObtainAuthTokenView.as_view(), name='obtain-auth-token'),

]


