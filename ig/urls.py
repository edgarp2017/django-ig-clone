from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
)

app_name = 'ig'

urlpatterns = [
    #URL: /
    path('', PostListView.as_view(), name='home'),
    path('new/', PostCreateView.as_view(), name='Create Post'),
    path('<int:id>', PostDetailView.as_view(), name='postDetail'),
]