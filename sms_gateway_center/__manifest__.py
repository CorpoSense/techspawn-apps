{
    'name': "SMS Gateway Center",

    'summary': """
        Sms Gateway Center helps you to configure Twilio and msg91 gateway""",

    'description': """

    """,

    'author': "Techspawn Solutions",
    'website': "http://www.techspawn.com",
    'images' : 'static/description/main.jpg',

    'category': 'SMS',
    'version': '1.1',

    'depends': ['base'],

    'data': [
        'views/single_sms_history.xml',
        'views/partner_view.xml',
        'views/gatway_auth.xml',
        'views/bulk_sms_view.xml',
        'views/bulk_history.xml',
        'wizard/single_sms.xml',
        'views/template_view.xml',
    ],

    'depends': ['base', 'sale'],
    'price': 25.00,
    'currency': 'EUR',
    'demo': [

    ],
    'images':['static/description/background.jpg'],
}
