# -*- coding: utf-8 -*-
{
    'name': "enrollment_main",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        - Student
        - Subject
        - Faculty
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
#         'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/teacher_view.xml',
        'views/parent_view.xml',
        'views/models_view.xml',
        'data/ir.sequence.csv',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}