from django.urls import path
from accounts.views import UserCreateView

app_name = "accounts"

urlpatterns = [
    path('registration/', UserCreateView.as_view(), name='registration'),
]