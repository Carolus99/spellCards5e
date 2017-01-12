"""SpellCards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url

from django.views.static import serve
from main_app import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^user/(\w+)/$', views.profile, name='profile'),

    url(r'^([0-9]+)/$', views.detail, name = 'detail'),

    url(r'post_url/$', views.post_spell, name='post_spell'),

    url(r'^login/$', views.login_view, name='Login'),

    url(r'^search/$', views.search, name='search'),

    url(r'^logout/$', views.logout_view, name='Logout')

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
