from django.shortcuts import render, redirect
from .models import Perfil, Habilidad, Educacion, ExperienciaLaboral, Proyecto, Contacto


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
    perfil = Perfil.objects.all()
    
    if request.method == 'POST':
        Contacto.objects.create(
            nombre  = request.POST.get('nombre'),
            correo  = request.POST.get('correo'),
            motivo  = request.POST.get('motivo'),
            mensaje = request.POST.get('mensaje'),
        )
        return redirect('contacto')

    return render(request, 'core/contacto/contacto.html', {'perfil': perfil})


