"""RadioChannel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from stream.views import Home,About,List_Podcast,Detail
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',Home.as_view(),name="home"),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts') ),
    re_path(r'^live/$',  views.TestPage.as_view(), name ="live"),
    re_path(r'^thanks/$',  views.ThanksPage.as_view(), name ="thanks"),
    re_path(r'^about/$', About.as_view(), name="about"),
    re_path(r'^list/$',List_Podcast.as_view(), name="list"),
    re_path(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name="detail"),
]
