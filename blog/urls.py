from django.urls import path
from django.views.generic.base import TemplateView
from . import views as vw

urlpatterns = [
    path('', vw.home, name='home'),
    path('list/', vw.PostListView.as_view(), name='list'),
    path('post/<slug:slug>/', vw.PostDetailView.as_view(), name='post_detail'),
    path('about/', vw.AboutView.as_view(), name='about'),
    path('resume/', vw.ResumeView.as_view(), name='resume'),
    path('project/', vw.ProjectListView.as_view(), name='projects'),
    path('project/<slug:slug>/',
         vw.ProjectDetailView.as_view(), name='project_detail'),
    path('category/<slug:category_slug>/',
         vw.project_by_category, name='project_by_cat'),
    path('resume2/', TemplateView.as_view(template_name='pages/resum.html'), name='resume2'),
]
