from django.contrib import admin
from .models import Blog, Liked, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', "title", "image", "created_at",]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]
    
admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', "blog", "content", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["content"]
    
admin.site.register(Comment, CommentAdmin)
    
class Likeadmin(admin.ModelAdmin):
    list_display = ['id', "like", 'blog', "created_at",]
    list_filter = ["created_at"]

admin.site.register(Liked, Likeadmin)

