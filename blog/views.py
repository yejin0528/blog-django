from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = "-pk"

    def get_context_data(self, **kwargs):  #재정의 ex)post_list
        context = super(PostList, self).get_context_data()
        context["categories"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()

        return context


class PostDatail(DetailView):
    model = Post
