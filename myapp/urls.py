"""electronic_certification URL Configuration

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
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'
urlpatterns = [
                  # http://127.0.0.1:8000/
                  url(r'^$', views.login, name='login'),
                  # http://127.0.0.1:8000/index/
                  url(r'^index$', views.index, name='index'),

                  # http://127.0.0.1:8000/person/
                  url(r'^person$', views.person, name='person'),

                  # http://127.0.0.1:8000/upload/
                  url(r'^upload$', views.upload, name='upload'),
                  # http://127.0.0.1:8000/upload_sfz/
                  url(r'^upload_sfz$', views.upload_sfz, name='upload_sfz'),
                  # http://127.0.0.1:8000/upload_yyzz/
                  url(r'^upload_yyzz$', views.upload_yyzz, name='upload_yyzz'),

                  # http://127.0.0.1:8000/see/
                  url(r'^see$', views.see, name='see'),
                  # http://127.0.0.1:8000/see_sfz/
                  url(r'^see_sfz$', views.see_sfz, name='see_sfz'),
                  # http://127.0.0.1:8000/see_yyzz/
                  url(r'^see_yyzz$', views.see_yyzz, name='see_yyzz'),
                  # 用户
                  url(r'^login$', views.login, name='login'),
                  url(r'^login_check$', views.login_check, name='login_check'),
                  url(r'^logout$', views.logout, name='logout'),

                  # 注册
                  url(r'^register/$', views.register, name='register'),
                  url(r'^register_handle/$', views.register_handle, name='register_handle'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
