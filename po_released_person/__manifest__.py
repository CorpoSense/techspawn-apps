# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Issued Person Name",
    'version': '0.1',
    'summary': """Issued by Field in Purchase Order and RFQ.""",
    'description': """
    """,
    'author': 'Techspawn Solutions Pvt. Ltd.',
    'company': 'Techspawn Solutions Pvt. Ltd.',
    'website': 'https://www.techspawn.com',
    'category': 'Purchase',
    'images': ['static/description/background.jpg'],
    'depends': ['purchase'],
    'license': 'LGPL-3',
    'data': [
        'views/views.xml',
        'views/purchase_order_report.xml',
        'views/purchase_quotation_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}