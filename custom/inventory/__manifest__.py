# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inventory Management',
    'author': 'Odoo S.A.',
    'version': '1.1',
    'summary': 'Inventory',
    'description': "",
    'website': '',
    'depends': ['stock','base'],
    'category': 'Warehouse',
    'sequence': 13,
    'demo': [
    ],
    'data': [
        'reports/report_inherit.xml',
        'reports/report_stock.xml',
    ],
    'qweb': [
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': '',
    'post_init_hook': '',
}
