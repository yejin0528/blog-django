from django.contrib import admin
from .models import Category, Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
