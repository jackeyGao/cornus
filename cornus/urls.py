"""cornus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from web.views import ListDetailView, IndexListView, PoetryDetailView, SearchListView, AboutView
from web.views import LoginView
from web.views import RegisterView
from web.views import LogoutView
from web.views import ProfileView
from web.views import ListView

urlpatterns = [
    url(r'^$', IndexListView.as_view(), name="index"),
    #url(r'^test/$', test),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^me/$', ProfileView.as_view(), name="me"),
    url(r'^search/', SearchListView.as_view(), name="search-list"),
    url(r'^list/$', ListView.as_view(), name="list"),
    url(r'^list/(?P<pk>.*)/$', ListDetailView.as_view(), name="list-detail"),
    url(r'^poetry/(?P<pk>.*)/', PoetryDetailView.as_view(), name="poetry-detail"),
    #url(r'^list/(?P<tag_name>.*)/', list_view),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

