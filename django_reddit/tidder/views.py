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

class Comment_Vote(viewsets.ModelViewSet):
    queryset = Comment_Vote.objects.all()
    serializer_class = Comment_VoteSerializer

class Save(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer

class Post_Vote(viewsets.ModelViewSet):
    queryset = Post_Vote.objects.all()
    serializer_class = Post_Vote