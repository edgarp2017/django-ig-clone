from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)

class PostListView(ListView):
    template_name = "ig/Home.html"
    queryset = Post.objects.all().filter(date__lte=timezone.now()).order_by('-date')
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'ig/create_post.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.username = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'ig/postDetail.html'
    queryset = Post.objects.all().filter(date__lte=timezone.now())
    slug_field = 'id'
    slug_url_kwarg = 'id'
    
    def get_obect(self):
        id_ = self.kwargs.get(id)
        return get_object_or_404(Post, id=id_)