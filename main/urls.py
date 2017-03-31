from django.conf.urls import url, include

from .views import home, auth

app_name = 'main'

urlpatterns = [
    url(r'^$', home.HomeView.as_view()),
    url(r'^login', auth.login, name='login'),
    url(r'^logout', auth.logout, name='logout'),
    url(r'^signup', auth.logout, name='signup'),
    url(r'^profile/', include('profile.urls'))
]
