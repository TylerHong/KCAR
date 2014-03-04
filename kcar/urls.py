from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from newcar import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^kcar/admin/', include(admin.site.urls)),
  url(u'^kcar/carlist/$', views.CarList.as_view(), name='carlist'),
  url(u'^kcar/carlist/(?P<mcode>[a-zA-Z]+)/$', views.CarList.as_view(), name='carlist'),
  url(u'^kcar/carlist/(?P<mcode>[a-zA-Z]+)/(?P<ccode>[a-zA-Z]+)/$', views.CarList.as_view(), name='carlist'),
    # Examples:
    # url(r'^$', 'kcar.views.home', name='home'),
    # url(r'^kcar/', include('kcar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns)
