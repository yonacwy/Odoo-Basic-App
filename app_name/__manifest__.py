# -*- coding: utf-8 -*-
{
    'name': 'App Name',
    'summary': """Something about the App.""",
    'version': '17.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': ['data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'reports/report_paper_format.xml',
        'reports/my_model_name_report.xml',
        'wizards/my_model_name_wizard.xml',
        'views/my_model_name_view.xml',
        'views/menus.xml'],
    'images': ['static/description/banner.png'],
    'icon': '/app_name/static/description/icon.png',
    'qweb': ['static/src/xml/*.xml'],
    'assets': {
        'web.assets_backend': [
            ('include', 'app_name/static/src/css/web_assets_backend.css'),
            ('include', 'app_name/static/src/js/web_assets_backend.js'),
        ],
        'web.assets_frontend': [
            ('include', 'app_name/static/src/css/web_assets_frontend.css'),
            ('include', 'app_name/static/src/js/web_assets_frontend.js'),
        ],
        'web.assets_common': [
            ('include', 'app_name/static/src/css/web_assets_common.css'),
            ('include', 'app_name/static/src/js/web_assets_common.js'),
        ],
    },
    'demo': ['demo/my_model_name_demo.xml'],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
