from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^subject/$', views.blog_subject_all, name='blog_subject_all'),
    url(r'^subject/(?P<url>.+)/$', views.subject_detail, name='subject_detail'),
    url(r'^get_subjects/$', views.get_subjects, name='blog_get_subjects'),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

]
