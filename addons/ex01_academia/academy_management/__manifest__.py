{
    'name': "Academy Management",
    'version': '1.0',
    'category': 'Education',
    'summary': 'Module for academy management',
    'description': """
        Academy Management Module
        =========================
        Manage students, courses, and enrollments.
    """,
    'depends': ['base'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/academy_data.xml',
        'views/academy_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': 'Noel González',
}