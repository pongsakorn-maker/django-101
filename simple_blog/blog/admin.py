from django.contrib import admin

from .models import Blog
from comments.models import Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    fields = ['is_spam', 'comment', 'created_by']
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_by', 'created_by']
    search_fields = ['title', 'content']
    list_filter = ['created']
    inlines = [CommentInLine]
