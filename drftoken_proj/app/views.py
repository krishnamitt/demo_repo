from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class LoginTokenAPI(APIView):
    def post(self, request):
        username = request.data.get("username")

        user, _ = User.objects.get_or_create(username=username)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key
        })


class ProfileTokenAPI(APIView):
    def get(self, request):
        token = request.headers.get("Authorization")

        if not token:
            return Response({"error": "Token missing"}, status=401)

        token_key = token.split()[1]
        token_obj = Token.objects.get(key=token_key)

        username = token_obj.user.username
        role = "Admin" if username == "murali" else "Employee"

        return Response({
            "username": username,
            "role": role
        })

class AboutTokenAPI(APIView):
    authentication_classes = []   
    permission_classes = []

    def get(self, request):
        return Response({
            "about": "Abacus Insights manages healthcare data by breaking down data silos and enabling secure analytics to improve outcomes."
        })
