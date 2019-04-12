from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('created_at', 'content', 'vote_total', 'post')

class PostSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('created_at', 'title picture', 'content', 'site_url', 'vote_total')