from django.contrib import get_user_model
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'title',
            'author',
            'body',
            'created_at',
            )
        model=Post
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=("id","username",)
        
    