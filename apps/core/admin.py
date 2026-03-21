from django.contrib import admin
from .models import Contacto, Perfil, ExperienciaLaboral, Educacion, Habilidad, Proyecto
# Register your models here.


admin.site.register(Perfil)
admin.site.register(ExperienciaLaboral)
admin.site.register(Educacion)
admin.site.register(Habilidad)
admin.site.register(Proyecto)
admin.site.register(Contacto)


"""
orden de llenado de datos desde el panel administrativo:
Perfils → primero crea tu perfil
Habilidads → asocia al perfil
Educacións → asocia al perfil
Experiencia Laborals → asocia al perfil
Proyectos → asocia al perfil
Contactos → lo llenan los visitantes solos

"""



""""
Modificaciones del panel administrativo de Django"""    
admin.site.site_header = "Panel administrativo - Portafolio Personal"
admin.site.site_title = "Portafolio Personal"
admin.site.index_title = "Panel Administrativo"
