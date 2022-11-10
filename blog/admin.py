from django.contrib import admin
from .models import Post, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "status", "published", "created", "updated"]
    list_filter = ["author", "status", "category"]
    search_fields = ["title", "category", "author"]
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)