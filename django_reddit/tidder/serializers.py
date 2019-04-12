from rest_framework import serializers

from .models import Post, Comment, User, Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('created_at', 'title picture', 'content', 'site_url', 'vote_total')
        
class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=False, read_only=True)
    class Meta:
        model = Comment
        fields = ('created_at', 'content', 'vote_total', 'post')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('profile_pic', 'user')

 class Post_VoteSerializer(serializer.ModelSerializer):
     post = PostSerializer(many=True, read_only=True)
     class Meta:
         model = Post_Vote
         fields = ('user, post, value')

class SaveSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    post = PostSerializer(many= True, read_only=True)
    class Meta:
        model = Save
        fields = ('user', 'post', 'created_at')

class Comment_VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True )
    class Meta:
        model = Comment_Vote
        fields = ('user', 'comment', 'value')

