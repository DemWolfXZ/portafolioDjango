# 🐺 Portafolio Personal — Alejandro Villa (DemWolf)

Portafolio personal desarrollado como proyecto del curso de Python con Django.
Permite gestionar y mostrar información profesional como habilidades, experiencia,
educación y proyectos, todo administrado desde un panel de administración conectado
a una base de datos SQLite.

---

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.13 + Django 6.0
- **Base de datos:** SQLite
- **Frontend:** HTML5 + CSS3 + Bootstrap 4
- **Iconos:** Font Awesome 4
- **Template:** Tunis Personal Portfolio

---

## 📁 Estructura del Proyecto
```
portafolio-django/
├── apps/
│   └── core/
│       ├── models.py        # Modelos: Perfil, Habilidad, Educacion, ExperienciaLaboral, Proyecto, Contacto
│       ├── views.py         # Vistas: index, nosotros, portafolio, contacto
│       ├── urls.py          # URLs de la app
│       └── admin.py         # Registro de modelos en el admin
├── config_portafolio/
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py
├── static/                  # Archivos estáticos (CSS, JS, imágenes)
├── templates/               # Templates HTML
│   ├── base.html
│   └── core/
│       ├── inicio.html
│       ├── nosotros/
│       ├── portafolio/
│       ├── contacto/
│       
├── media/                   # Imágenes subidas desde el admin (autogenerado)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalación y Configuración

### 1 — Clonar el repositorio
```bash
git clone https://github.com/DemWolfXZ/portafolioDjango.git
cd portafolioDjango
```

### 2 — Crear y activar entorno virtual
```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac / Linux
python -m venv env
source env/bin/activate
```

### 3 — Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4 — Aplicar migraciones
```bash
python manage.py migrate
```

### 5 — Crear superusuario para el panel de administración
```bash
python manage.py createsuperuser
```

### 6 — Levantar el servidor de desarrollo
```bash
python manage.py runserver
```

---

## 🌐 Acceso al Sitio

| URL | Descripción |
|-----|-------------|
| http://127.0.0.1:8000 | Página de inicio |
| http://127.0.0.1:8000/nosotros | Sobre mí — habilidades, experiencia y educación |
| http://127.0.0.1:8000/portafolio | Proyectos |
| http://127.0.0.1:8000/contacto | Formulario de contacto |
| http://127.0.0.1:8000/admin | Panel de administración |

---

## 📋 Cargar Datos desde el Admin

Una vez levantado el servidor, ingresar al panel admin en:
**http://127.0.0.1:8000/admin**

Crear los siguientes registros en orden:

### 1. Perfil
Campo | Descripción
------|------------
Nombre / Apellido | Nombre completo
Edad / Nacionalidad | Datos personales
Freelance | Disponibilidad (booleano)
Dirección / Teléfono / Correo | Datos de contacto
Idiomas | Ej: Español, Inglés
Profesión | Ej: Ingeniero Informático
Descripción | Texto de presentación en el inicio
Foto | Imagen de perfil (se muestra en inicio y nosotros)
Años experiencia / Clientes / Proyectos / Premios | Contadores estadísticos

### 2. Habilidades
Asociar al perfil creado. Campos: nombre de la habilidad y porcentaje (0-100).
Ej: `Python — 85`

### 3. Educación
Asociar al perfil. Campos: institución, título y año de graduación.

### 4. Experiencia Laboral
Asociar al perfil. Campos: empresa, cargo, duración y detalles del cargo.

### 5. Proyectos
Asociar al perfil. Campos: título, descripción, tecnologías, URL demo, URL repositorio, imagen y si es destacado.

---

## 🗄️ Modelos de la Base de Datos
```python
Perfil           # Datos personales y contadores estadísticos
Habilidad        # Habilidades técnicas con porcentaje (FK → Perfil)
Educacion        # Títulos y certificaciones (FK → Perfil)
ExperienciaLaboral  # Historial laboral (FK → Perfil)
Proyecto         # Proyectos del portafolio (FK → Perfil)
Contacto         # Mensajes recibidos desde el formulario (independiente)
```

---

## 📦 Dependencias

Ver archivo `requirements.txt`. Las principales son:
```
asgiref==3.11.1
Django==6.0.3
pillow==12.1.1
psycopg==3.3.3
psycopg-binary==3.3.3
sqlparse==0.5.5
tzdata==2025.3

```

---

## 👨‍💻 Autor

**Alejandro Villa** — DemWolf  
🔗 [GitHub](https://github.com/DemWolfXZ)  
🔗 [LinkedIn](https://www.linkedin.com/in/alejandro-villa-villavicencio/)  
🎵 [YouTube](https://www.youtube.com/@DemWolf.IAmusic)  

---

## 📝 Notas

- Este proyecto fue desarrollado como entrega del **Módulo 8** del curso de Python con Django.
- La base de datos no se incluye en el repositorio — debe generarse localmente con `python manage.py migrate`.
- Las imágenes subidas desde el admin se almacenan en la carpeta `media/` que se genera automáticamente.