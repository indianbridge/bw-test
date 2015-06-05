from django.conf.urls import include, url
from . import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	
	# api
    url(r'^api/v1/posts/$', views.post_collection),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.post_element),
	url(r'^api/v1/users/$', views.ListUsers.as_view()),
	url(r'^api/v1/get-auth-token/', rest_views.obtain_auth_token),
]
