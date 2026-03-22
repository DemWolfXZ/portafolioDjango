from django.shortcuts import render, redirect
from .models import Perfil, Habilidad, Educacion, ExperienciaLaboral, Proyecto, Contacto
from .forms import ContactoForm

# =============================================================================
# Inicio — Datos básicos del perfil para la página principal
# =============================================================================
def index(request):
    perfil = Perfil.objects.first()
    #perfil = Perfil.objects.all()

    context = {
        'perfil': perfil,
    }
    return render(request, 'core/inicio.html', context)


# =============================================================================
# Nosotros — Datos personales, contadores, habilidades, educación y experiencia
# =============================================================================
def nosotros(request):
    # .first() retorna un objeto único, no un queryset
    perfil      = Perfil.objects.first()
    habilidades = Habilidad.objects.all()
    educacion   = Educacion.objects.all()
    experiencia = ExperienciaLaboral.objects.all()

    context = {
        'perfil':      perfil,       
        'habilidades': habilidades,
        'educacion':   educacion,
        'experiencia': experiencia,
    }
    return render(request, 'core/nosotros/nosotros.html', context)


# =============================================================================
# Portafolio — Lista de proyectos (destacados primero)
# =============================================================================
def portafolio(request):
    # perfil = Perfil.objects.first()
    proyectos = Proyecto.objects.all()

    context = {
        'proyectos': proyectos,
    }
    return render(request, 'core/portafolio/portafolio.html', context)


# =============================================================================
# Contacto — Muestra el formulario y guarda el mensaje en la BD
# =============================================================================
def contacto(request):
    # Objeto único del perfil para mostrar datos de contacto
    perfil = Perfil.objects.first()

    # Form vacío por defecto — se inicializa ANTES del if POST
    form = ContactoForm()

    if request.method == 'POST':
        # Si es POST llenamos el form con los datos enviados
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardamos el mensaje en la BD
            form.save()
            return redirect('contacto')

    context = {
        'perfil': perfil,
        'form':   form,
    }
    return render(request, 'core/contacto/contacto.html', context)