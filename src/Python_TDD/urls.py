from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Python_TDD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_page, name='home'),
)