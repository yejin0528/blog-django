from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_img = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_uploead = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self):
        return f"/blog/{self.pk}"
