# models.py
from django.db import models
from decimal import Decimal

class Mobil(models.Model):
    nama = models.CharField(max_length=100)
    merk = models.CharField(max_length=100, default='Merk Default')
    model = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=30, decimal_places=6)
    tahun = models.IntegerField()
    harga_dasar = models.DecimalField(max_digits=30, decimal_places=6, default=0)  # Tambahkan nilai default
    pinjaman_dana_bank = models.DecimalField(max_digits=30, decimal_places=6, default=0)
    suku_bunga_bank = models.FloatField()

    def hitung_hpp(self):
        try:
            pinjaman = self.pinjaman_dana_bank or Decimal('0')
            bunga = Decimal(str(self.suku_bunga_bank)) or Decimal('0')
            total_service = sum(service.biaya for service in self.services.all())

            denominator = pinjaman + bunga
            if denominator == 0:
                return None  # Hindari pembagian nol

            hpp = (self.harga_dasar / denominator) + total_service
            return round(hpp, 2)
        except Exception as e:
            return None  # 


    def __str__(self):
        return f"{self.nama} - {self.merk} ({self.tahun})"
    
class Service(models.Model):
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE, related_name='services')
    tanggal_service = models.DateField()
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=30, decimal_places=6)

    def __str__(self):
        return f"Service {self.mobil.nama} pada {self.tanggal_service}"

