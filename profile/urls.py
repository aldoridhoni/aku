from django.conf.urls import url

from .views import avatar, profile, ssh

urlpatterns = [url(r'$', profile.overview, name='profile_overview'), ]
