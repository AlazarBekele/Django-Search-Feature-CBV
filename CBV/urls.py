from django.urls import path
from .views import find_post

urlpatterns = [
    path ('', find_post, name='post_list')
]
