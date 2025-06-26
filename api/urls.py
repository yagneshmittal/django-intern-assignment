from django.urls import path
from .views import public_api, protected_api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('public/', public_api, name='public-api'),
    path('protected/', protected_api, name='protected-api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from .views import list_telegram_users
path('telegram-users/', list_telegram_users),
