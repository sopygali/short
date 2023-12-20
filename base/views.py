from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, RetrieveDestroyAPIView
from .models import Logins
import pyshorteners
from .serializers import LoginSerializer, LoginAPISerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import MyUserCreationForm
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

class Login(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Logins.objects.all()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user.id) #todo user=request.JWT.user) #self.filter_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) #пока что он как то не так берет queryset

    def create(self, request): #todo user?
        request.data['user'] = request.user.id
        #shortlink = pyshorteners.Shortener().tinyurl.short(request.data['link'])
        #request.data['link'] = shortlink
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class LoginAPIDestroy(RetrieveDestroyAPIView):
    queryset = Logins.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated, )

class LoginAPI(APIView):
    def post(self, request):

        data = request.data
        serializer = LoginAPISerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is None:
                return Response({
                    'status': 400
                })

            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })


class RegisterAPI(APIView):

    def post(self, request):
        try:
            serializer = MyUserCreationForm(request.data)
            if serializer.is_valid():
                user = serializer.save()
                login(request, user)
                return Response({
                    'status': 200,
                    'message': 'succesfully registered'
                })

            return Response({
                'status': 400,
                'message': 'incorrect values'
            })

        except Exception:
            print(Exception)
