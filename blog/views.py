from django.views.generic import ListView

from blog.models import Blog


class BlogCreateView(ListView):
    model = Blog
    fields = ('title', 'body',)