from django.contrib import admin
from .models import Categorie, Post, Author, Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'active']
    list_filter = ['categorie', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author']


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published']
    prepopulated_fields = {'slug': ('title', )}
