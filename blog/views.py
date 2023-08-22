from typing import Any, Dict
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Post, Project, Categorie


def home(request):
    posts = Post.objects.all()[:3]
    context = {
        'posts': posts,
    }
    return render(request, 'pages/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'pages/post-detail.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ResumeView(TemplateView):
    template_name = 'pages/resume.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'pages/project.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categorie.objects.all()
        context['categories'] = categories
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pages/project_detail.html'
    context_object_name = 'project'


def project_by_category(request, category_slug):
    projects = Project.objects.filter(slug=category_slug)
    print(projects)
    context = {
        'projects': projects,
    }
    return render(request, 'pages/project_by_cat.html', context)


def project_by_category(request, category_slug):
    categorie = Categorie.objects.all()
    category = get_object_or_404(Categorie, slug=category_slug)
    projects = Project.objects.filter(category=category)
    context = {
        'projects': projects,
        'category': category,
        'categories': categorie,
    }
    return render(request, 'pages/project_by_cat.html', context)
