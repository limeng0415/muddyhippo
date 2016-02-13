from django.conf.urls import include, url
from django.contrib import admin
from testWeb.view import hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'testWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
]
