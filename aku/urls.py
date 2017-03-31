from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from main.views import home

# admin.autodiscover()

urlpatterns = [
    # static page
    url(r'^$', home.HomeView.as_view()),
    url(r'^privacy.html', TemplateView.as_view(template_name='privacy.html')),
    # dynamic page
    # url(r'^o/', include('openid_provider.urls')),
    url(r'^accounts/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)),
                   ] + urlpatterns
