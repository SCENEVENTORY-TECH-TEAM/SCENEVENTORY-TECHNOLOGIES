from django.urls import path
from .views import UserInfoAPIView, UserInfoDetails
urlpatterns = [
    path('users/', UserInfoAPIView.as_view()),
    path('users/<int:id>/', UserInfoDetails.as_view()),
]
