from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get("username")
        request.session['username'] = username
        return Response({"message": "Logged in"})


class ProfileAPI(APIView):
    def get(self, request):
        username = request.session.get("username")

        if not username:
            return Response({"error": "Not logged in"}, status=401)

        role = "Admin" if username == "murali" else "Employee"

        return Response({
            "username": username,
            "role": role
        })

class AboutAPI(APIView):
    authentication_classes = []   
    permission_classes = []

    def get(self, request):
        return Response({
            "about": "Abacus Insights manages healthcare data by breaking down data silos and enabling secure analytics to improve outcomes."
        })
