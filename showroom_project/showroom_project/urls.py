from django.contrib import admin
from django.urls import path, include  # 'include' digunakan untuk menyertakan file urls.py dari aplikasi lain

urlpatterns = [
    path('admin/', admin.site.urls),  # Akses halaman admin
    path('', include('mobil_showroom.urls')),  # Arahkan ke file urls.py dari aplikasi 'mobil_showroom'
]
