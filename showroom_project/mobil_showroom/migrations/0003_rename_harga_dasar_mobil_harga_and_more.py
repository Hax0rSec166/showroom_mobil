# Generated by Django 5.2 on 2025-04-18 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobil_showroom', '0002_remove_mobil_dana_bank_remove_mobil_suku_bunga_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobil',
            old_name='harga_dasar',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='mobil',
            old_name='merk',
            new_name='nama',
        ),
        migrations.RemoveField(
            model_name='mobil',
            name='model',
        ),
        migrations.RemoveField(
            model_name='mobil',
            name='pinjaman_dana_bank',
        ),
        migrations.RemoveField(
            model_name='mobil',
            name='suku_bunga_bank',
        ),
        migrations.RemoveField(
            model_name='mobil',
            name='tahun',
        ),
    ]
