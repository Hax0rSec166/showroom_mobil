from django import forms
from .models import Mobil, Service

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = '__all__'
        widgets = {
            'suku_bunga_bank': forms.NumberInput(attrs={
                'step': 'any',
                'min': '0',
                'max': '100',
                'style': 'width: 100px;',
                'placeholder': 'Masukkan persen',
            }),
            'pinjaman_dana_bank': forms.NumberInput(attrs={
                'step': 'any',
                'min': '0',
                'style': 'width: 150px;',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['suku_bunga_bank'].label = 'Suku bunga bank (%)'
        self.fields['pinjaman_dana_bank'].label = 'Pinjaman dana bank (Rp)'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'tanggal_service': forms.DateInput(attrs={'type': 'date'}),
            'biaya': forms.NumberInput(attrs={'step': 'any'}),
        }
