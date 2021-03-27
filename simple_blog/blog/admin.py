from django.contrib import admin

from .models import Blog

# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_by','created_by']
    search_fields =['title', 'content']
    list_filter= ['created']