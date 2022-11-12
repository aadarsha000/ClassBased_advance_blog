from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "status", "published", "created", "updated"]
    list_filter = ["author", "status", "category"]
    search_fields = ["title", "category", "author"]
    prepopulated_fields = {"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "post"]

admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)