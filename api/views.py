from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .models import *

from .serializers import ArticleSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    Creating Article ViewSet for create Article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
