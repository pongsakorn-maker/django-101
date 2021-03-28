from django.contrib import admin

from .models import Comment

# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created', 'created_by', 'blog', 'is_spam']
    list_filter = ['created']
