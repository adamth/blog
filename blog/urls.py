from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^register/$', views.register, name='register'),
    url(r'^signin/', views.sign_in, name='sign_in'),
    url(r'^signout/', views.sign_out, name='sign_out'),
    url(r'^post/(?P<pk>\d+)/like/$', views.post_like, name='post_like'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
]
