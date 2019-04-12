from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, UserSerializer, ProfileSerializer
from .models import Post, Comment, User, Profile


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Comment(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Profile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
