# UF1889 - Prácticas Odoo

Repositorio de ejercicios y prácticas del módulo UF1889 de desarrollo con Odoo.

## Contenido

### Ejercicios
- `ejercicios/ex01_modelos_relaciones.md` - Ejercicio 1: Identificar modelos y relaciones 1-N

### Módulos Odoo
- `addons/ex01_academia/academy_management` - Módulo de gestión de academia

## Módulo: Academy Management

Módulo que implementa la gestión de estudiantes y tutorías con relación 1-N.

### Características
- Modelo `academy.student` (entidad principal)
- Modelo `academy.tutoring` (actividad/detalle)
- Campos computados para estadísticas
- Vistas compatibles con Odoo 17+/18/19

### Instalación
1. Copiar a la carpeta `addons` de Odoo
2. Actualizar lista de módulos
3. Instalar "Academy Management"

## Requisitos

- Odoo 17+ (probado con Odoo 19)
- Python 3.x