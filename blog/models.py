from ast import mod
from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_thumbnail = models.ImageField()

    def __str__(self):
        return self.user.username


class Categorie(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=20)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    overview = RichTextUploadingField()
    content = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='post_thumbnail')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categorie = models.ManyToManyField(Categorie)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    overview = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='project_img')
    content = RichTextUploadingField()
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = TaggableManager()
    category = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.title[:30] + "..."

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})
