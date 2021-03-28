from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogModelSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']


class BlogListApiView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogListApiGenericView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogInstanceApiView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "id"
