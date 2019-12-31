# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    # status = 1 means post has been published
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
