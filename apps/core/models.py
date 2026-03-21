# =============================================================================
# Estructura basada en los datos del views.py del profe, pero cargados desde BD.
# =============================================================================

from django.db import models


# --- Opciones reutilizables ---------------------------------------------------

NIVEL_CHOICES = [
    ('basico',      'Básico'),
    ('intermedio',  'Intermedio'),
    ('avanzado',    'Avanzado'),
    ('experto',     'Experto'),
]


# =============================================================================
# Perfil — Modelo central, equivalente al dict 'professional' y 'experience'
# del profe. Todos los demás modelos dependen de este.
# =============================================================================
class Perfil(models.Model):
    # Datos personales — equivalente a 'professional' del profe
    nombre            = models.CharField(max_length=50)
    apellido          = models.CharField(max_length=50)
    edad              = models.IntegerField()
    nacionalidad      = models.CharField(max_length=50)
    freelance         = models.BooleanField(default=True)
    direccion         = models.CharField(max_length=150, blank=True)
    telefono          = models.CharField(max_length=20, blank=True)
    correo            = models.EmailField(unique=True)
    idiomas           = models.CharField(max_length=100, blank=True)  # Ej: "Español, Inglés"
    profesion         = models.CharField(max_length=100, blank=True)  # Ej: "Desarrollador de Software"
    descripcion       = models.TextField(blank=True)
    foto              = models.ImageField(upload_to='perfil/', blank=True, null=True)

    # Contadores — equivalente a 'experience' del profe
    anios_experiencia = models.IntegerField(default=0)
    clientes_felices  = models.IntegerField(default=0)
    proyectos_count   = models.IntegerField(default=0)
    premios           = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =============================================================================
# Habilidad — Equivalente a la lista 'skills' del profe
# Usa porcentaje directo en lugar de nivel de texto
# =============================================================================
class Habilidad(models.Model):
    perfil     = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='habilidades')
    nombre_habilidad     = models.CharField(max_length=100)
    porcentaje = models.IntegerField(default=0)  # 0-100, equivalente al 'porcentaje' del profe

    class Meta:
        ordering = ['-porcentaje']

    def __str__(self):
        return f"{self.nombre_habilidad} ({self.porcentaje}%)"


# =============================================================================
# Educacion — Relacionada con el Perfil
# =============================================================================
class Educacion(models.Model):
    perfil          = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='educacion')
    institucion     = models.CharField(max_length=150)
    titulo          = models.CharField(max_length=150)
    anio_graduacion = models.IntegerField()

    class Meta:
        verbose_name = 'Educación'

    def __str__(self):
        return f"{self.titulo} — {self.institucion}"


# =============================================================================
# ExperienciaLaboral — Relacionada con el Perfil
# =============================================================================
class ExperienciaLaboral(models.Model):
    perfil   = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='experiencias')
    empresa  = models.CharField(max_length=100)
    cargo    = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Experiencia Laboral'

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"


# =============================================================================
# Proyecto — Relacionado con el Perfil
# =============================================================================
class Proyecto(models.Model):
    perfil      = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='proyectos')
    titulo      = models.CharField(max_length=150)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200, blank=True)
    url_demo    = models.URLField(blank=True)
    url_repo    = models.URLField(blank=True)
    imagen      = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    destacado   = models.BooleanField(default=False)

    class Meta:
        ordering = ['-destacado']

    def __str__(self):
        return self.titulo


# =============================================================================
# Contacto — Independiente, lo llenan los visitantes del portafolio
# =============================================================================
class Contacto(models.Model):

  

    nombre  = models.CharField(max_length=100)
    correo  = models.EmailField()
    motivo  = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} — {self.motivo}"