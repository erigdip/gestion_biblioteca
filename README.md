# Módulo de Gestión de Biblioteca (Odoo 18)

Módulo personalizado para Odoo 18 desarrollado como proyecto académico.
Permite la gestión de libros, autores y el control de préstamos dentro de una biblioteca.

## Características
- **Gestión de Libros:** Registro detallado con Título, Autor, ISBN y sinopsis.
- **Base de Datos de Autores:** Relación directa con los libros.
- **Control de Préstamos:**
  - Estados visuales (Disponible / Prestado / Perdido).
  - Lógica de validación: El campo "Prestado a" es obligatorio si el libro se marca como prestado.
  - Automatización: Limpieza automática del prestatario al devolver el libro.
- **Interfaz Moderna:** Uso de vistas `list` (compatibles con Odoo 18), `search` con filtros y `statusbar`.

## Tecnologías
- **Lenguaje:** Python 3
- **Framework:** Odoo 18
- **Datos:** PostgreSQL

## Instalación
1. Clona este repositorio en tu carpeta de `custom_addons` de Odoo:
   ```bash
   git clone https://github.com/erigdip/gestion_biblioteca.git

2. Reinicia el servicio de Odoo.

3. Activa el "Modo Desarrollador" en Odoo.

4. Ve a Aplicaciones, haz clic en "Actualizar lista de aplicaciones". 

5. Instala el módulo de Biblioteca (gestion_biblioteca).