"""

BLOG APP URLS

"""
from django.conf.urls import url
from .views import (
	post_list, 
	post_create, 
	post_delete, 
	post_update, 
	post_home, 
	post_detail
	)

urlpatterns = [

	url(r'^$', post_list),
	url(r'^create/$', post_create),
	url(r'^delete/$', post_delete),
	url(r'^update/$', post_update),
	url(r'^detail/$', post_detail),

]
