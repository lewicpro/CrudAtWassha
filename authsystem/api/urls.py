"""Fingerprint URL Configuration

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
from rest_framework_jwt.views import obtain_jwt_token
from .views import  *


urlpatterns = [
    # url(r'^$', numberGetview.as_view(), name='numberCreate'),
    url(r'^UserCreate/$', CreateUserView.as_view(), name='nubergen'),
    # url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^authdata/$', authdataCreatelView.as_view(), name='data'),
    url(r'^names/$', nameslView.as_view(), name='data'),
    url(r'^names/(?P<pk>\d+)/$', nameslView.as_view(), name='data'),
    url(r'^api/auth/token-auth/', obtain_jwt_token),
    # url(r'^authdata/(?P<pk>\d+)/$', authdataModelView.as_view(), name='mor'),
 
  


]