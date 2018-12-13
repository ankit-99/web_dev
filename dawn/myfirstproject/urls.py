"""myfirstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from myapp.views import (restaurant_listview,
RstListview,
RstDetailView
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='base.html')),
    path('restaurant/', RstListview.as_view()),
   # url('restaurant/(?P<slug>\w+)/',RstListview.as_view()),
    url('restaurant/(?P<rest_id>\w+)/',RstDetailView.as_view()),
    #path('restaurant/jaipur/', Jprlocation.as_view()),
    #path('restaurant/alwar/', Awrlocation.as_view()),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html')),
]
