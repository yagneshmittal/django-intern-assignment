from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public endpoint."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello, {request.user.username}. You are authenticated!"})

from .models import TelegramUser

@api_view(['GET'])
def list_telegram_users(request):
    users = TelegramUser.objects.values('username', 'created_at')
    return Response(list(users))
