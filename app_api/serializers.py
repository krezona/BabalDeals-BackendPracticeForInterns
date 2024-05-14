from rest_framework import serializers
from app.models import Post
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title','image','slug', 'author','excerpt', 'content','status')

