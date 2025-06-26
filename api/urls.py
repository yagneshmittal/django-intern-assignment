from django.urls import path
from .views import public_api, protected_api, list_telegram_users
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('public/', public_api, name='public-api'),
    path('protected/', protected_api, name='protected-api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('telegram-users/', list_telegram_users, name='telegram-users'),
]
