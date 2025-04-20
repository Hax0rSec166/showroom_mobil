# views.py di dalam aplikasi mobil_showroom
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mobil
from .forms import MobilForm
from .models import Service

# Fungsi untuk menampilkan daftar mobil
def daftar_mobil(request):
    mobil_list = Mobil.objects.all()  # Mengambil semua data mobil
    return render(request, 'mobil_showroom/daftar_mobil.html', {'mobil_list': mobil_list})

# Fungsi untuk rincian mobil (READ-ONLY)
def rincian_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, pk=mobil_id)
    form = MobilForm(instance=mobil)

    # Buat semua field hanya bisa dilihat, tidak bisa diubah
    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True

    return render(request, 'mobil_showroom/rincian_mobil.html', {'form': form, 'mobil': mobil})

# Fungsi Menampilkan ID 
def home(request):
    daftar_mobil = Mobil.objects.all()
    return render(request, 'home.html', {'daftar_mobil': daftar_mobil})

#Fungsi Menghapus Mobil
def hapus_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, pk=mobil_id)
    if request.method == 'POST':
        mobil.delete()
        return redirect('daftar_mobil')
    return redirect('rincian_mobil', mobil_id=mobil_id)

# Fungsi Menampilkan Semua Service Mobil
def service_detail(request, service_id):
    # Ambil data service berdasarkan ID
    service = get_object_or_404(Service, pk=service_id)
    
    # Kirim data service ke template
    return render(request, 'mobil_showroom/service_detail.html', {'service': service})
