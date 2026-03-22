from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model  = Contacto
        # Campos que coinciden exactamente con el modelo
        fields = ['nombre_remitente', 'correo_remitente', 'motivo', 'mensaje']
        widgets = {
            # Input nombre con placeholder y estilo del template
            'nombre_remitente': forms.TextInput(attrs={
                'placeholder': 'Nombre completo',
                'required':    True,
            }),
            # Input correo con placeholder y estilo del template
            'correo_remitente': forms.EmailInput(attrs={
                'placeholder': 'Correo electrónico',
                'required':    True,
            }),
            # Input motivo con placeholder y estilo del template
            'motivo': forms.TextInput(attrs={
                'placeholder': 'Motivo del contacto',
                'required':    True,
            }),
            # Textarea mensaje con placeholder y estilo del template
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje aquí...',
                'required':    True,
                'rows':        8,
            }),
        }