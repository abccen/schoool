from django.contrib.auth.hashers import check_password
from rest_framework import views, response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_app.serialisers import UserSerializer
from auth_app.models import MyUser


class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('email')
        if not MyUser.objects.filter(email=login):
            return Response({f'{login} - does not exist'})
        user = MyUser.objects.get(email=login)
        password = request.data.get('password')
        pass_check = check_password(password, user.password)
        if not pass_check:
            return Response({'password incorrect'})
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})
