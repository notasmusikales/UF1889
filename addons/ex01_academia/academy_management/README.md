# Academy Management

Módulo de gestión de academia para Odoo 19+.

## Descripción

Este módulo implementa la gestión de estudiantes y sus tutorías, demostrando la relación 1-N entre modelos en Odoo.

## Modelos

### academy.student (Entidad principal)
- `name` - Nombre del estudiante
- `email` - Correo electrónico
- `state` - Estado académico (draft/enrolled/graduated/dropped)
- `tutoring_ids` - Relación One2many hacia tutorías
- `tutoring_count` - Contador de tutorías (computado)
- `last_tutoring_date` - Fecha de última tutoría (computado)

### academy.tutoring (Actividad/Detalle)
- `name` - Asunto de la tutoría
- `date` - Fecha de la tutoría
- `notes` - Notas
- `student_id` - Relación Many2one hacia estudiante

## Relación 1-N

La relación lógica del negocio:
- Un estudiante puede tener muchas tutorías
- Una tutoría pertenece a un solo estudiante

Implementación en Odoo:
- En `academy.tutoring`: Many2one hacia `academy.student`
- En `academy.student`: One2many hacia `academy.tutoring`

## Instalación

1. Copiar el módulo a la carpeta `addons` de Odoo
2. Actualizar la lista de módulos en Odoo
3. Buscar "Academy Management" e instalar

## Estructura

```
academy_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── tutoring.py
├── views/
│   └── academy_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── res_groups.xml
└── README.md
```

## Compatibilidad

- Odoo 17+
- Odoo 18
- Odoo 19