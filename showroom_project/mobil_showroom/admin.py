from django.contrib import admin
from .models import Mobil, Service

@admin.register(Mobil)
class MobilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'merk', 'model', 'tahun', 'harga')
    search_fields = ('nama', 'merk', 'model')
    list_filter = ('tahun', 'merk')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('mobil', 'tanggal_service', 'biaya')
    search_fields = ('mobil__nama', 'tanggal_service')
    list_filter = ('tanggal_service',)
    date_hierarchy = 'tanggal_service'
