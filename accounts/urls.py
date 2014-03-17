from django.conf.urls import patterns, include, url
import accounts.views

urlpatterns = patterns('',
    url(r'^profile', accounts.views.profile, name='profile_page')
)