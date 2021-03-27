from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogModelSerializer


class BlogListApiView(APIView):
    def get(self,request,*args,**kwargs):
        blogs = Blog.objects.all()
        serializer = BlogModelSerializer(blogs,many=True)
        return Response(serializer.data)