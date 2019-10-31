"""Blog URL Configuration

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
from . import views

urlpatterns = [
    url(r'hello/$', views.hello),
    url(r'shop/$', views.shop, name='shop-index'),
    url(r'shop/creat/$', views.shopcreat, name='shop-creat'),
    url(r'shop/(?P<pk>\d+)$', views.shopupdate, name="shop-update"),
    url(r'shop/(?P<pk>\d+)/delete$', views.shopdelete, name="shop-delete"),

    # --- asset_repair_detail ---
    url(r'order/$', views.order, name='order-index'),
    url(r'order/creat/(?P<pk>\d+)$', views.ordercreat, name='order-creat'),
    url(r'order/detail/(?P<pk>\d+)$', views.orderdetail, name='order-detail'),
    url(r'order/detail/creat/(?P<pk>\d+)$', views.detailcreat, name='detail-creat'),
]
