from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'username', 'email']
        model = User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class TopicSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Topic


class ProjectSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Project
