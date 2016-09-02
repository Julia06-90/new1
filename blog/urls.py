from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'blog.views.chapter_index', name='chapter_index'),

    url(r'(\d+)/', 'blog.views.title'),
    url(r'^accounts/login/$',  'blog.views.login'),
    url(r'^accounts/logout/$', 'blog.views.logout'),
    url(r'^accounts/registration/$', 'blog.views.registration')
)
