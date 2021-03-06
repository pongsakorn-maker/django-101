from django.views.generic import DetailView, ListView, TemplateView

from .models import Blog


class SimpleBlogView(TemplateView):
    template_name = 'simple_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        my_blog = Blog.objects.get(id=kwargs.get('id'))
        context['title'] = my_blog.title
        context['content'] = my_blog.content
        context['created_by'] = my_blog.created_by
        context['created'] = my_blog.created
        return context


class SimpleBlogDetailView(DetailView):
    model = Blog
    pk_url_kwarg = 'id'
    context_object_name = 'blog'


class MultipleBlogView(ListView):
    model = Blog
    context_object_name = 'blogs'
