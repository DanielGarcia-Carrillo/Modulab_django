from django.conf.urls import patterns, include, url
import frontend.views

urlpatterns = patterns('',
    url(r'^$', frontend.views.main_page, name='main_page')
)