from django.conf.urls import patterns, url

from sq_web import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)