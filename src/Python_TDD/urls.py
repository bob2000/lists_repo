from django.conf.urls import patterns, include, url
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Python_TDD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
)
