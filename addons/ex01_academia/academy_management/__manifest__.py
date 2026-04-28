{
    'name': 'Academy Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Academy student and tutoring management',
    'description': """
        Academy Management Module
        ==========================
        This module manages students and their tutoring sessions.
        It implements a 1-N relationship between students and tutorings.
    """,
    'author': 'Academy',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/academy_views.xml',
    ],
    'application': False,
    'auto_install': False,
}