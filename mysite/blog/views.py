from django.shortcuts import render
from .models import Post
from django.views import generic


class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'


def home(request):
    return render(request, 'home.html')


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_create')
    template_name = 'posts.html'
