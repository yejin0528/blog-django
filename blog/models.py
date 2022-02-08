import os
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_img = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"[{self.pk}] {self.title} - {self.author}"

    def get_absolute_url(self):
        return f"/blog/{self.pk}"

    def get_file_name(self):  # file 이름
        return os.path.basename(self.file_upload.name)


class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"

    class Meta:
        verbose_name_plural = "Categories"
