# urls.py di dalam aplikasi mobil_showroom
from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_mobil, name='daftar_mobil'),
    path('hapus/<int:mobil_id>/', views.hapus_mobil, name='hapus_mobil'),
    path('rincian/<int:mobil_id>/', views.rincian_mobil, name='rincian_mobil'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
]
