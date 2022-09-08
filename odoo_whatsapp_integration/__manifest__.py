# -*- coding: utf-8 -*-
{
    'name': "Whatsapp Odoo Integration",

    'summary': """
       Whatsapp Odoo integration Whatsapp connector Whatsapp CRM Whatsapp sale order Whatsapp purchase order Whatsapp invoice Whatsapp delivery orders with order items to the respective user Whatsapp payment reminder Whatsapp point of sale whatsapp communicatio""",

    'description': """
        
    """,

    'author': "Techspawn Solutions Pvt. Ltd.",
    'website': "http://www.techspawn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Whatsapp',
    'version': '0.1',
    'license': 'OPL-1',
    'price': 10.00,
    'currency': 'USD',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web', 'stock', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
          'views/views.xml',
          'wizard/message_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'images':['static/description/Whatsapp.gif'],
}
