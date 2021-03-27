from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created = serializers.DateTimeField()
    # created = serializers.PrimaryKeyRelatedField()

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Blog
        fields = '__all__'