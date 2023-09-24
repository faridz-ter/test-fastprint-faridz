"""
URL configuration for test_fastprint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from produk import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('produk_filter/', views.produk_filter, name='produk_filter'),
    path('tambah_produk/', views.tambah_produk, name='tambah_produk'),
    path('edit_produk/<int:id_produk>/', views.edit_produk, name='edit_produk'),
    path('hapus_produk/<int:id_produk>/', views.hapus_produk, name='hapus_produk'),
]
