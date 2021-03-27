from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Blog


User = get_user_model()


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created = serializers.DateTimeField()


class BlogModelSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1
