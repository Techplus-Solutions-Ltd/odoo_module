# -*- coding: utf-8 -*-

{
    'name': 'Mollie Payments Extended',
    'version': '18.0.0.1',
    'category': 'eCommerce',
    'license': 'LGPL-3',
    'author': 'Mollie',
    'maintainer': 'Droggol Infotech Private Limited',
    'website': 'https://www.mollie.com/',

    'summary': 'Add extra features in mollie payment',
    'description': """
        Add extra features in mollie payment
    """,

    'depends': [
        'payment_mollie', 'product', 'account', 'base_automation'
    ],
    'external_dependencies': {},
    'data': [
        'data/cron.xml',
        'security/ir.model.access.csv',
        'views/payment_views.xml',
        'views/payment_transaction.xml',
        'views/payment_method.xml',
        'views/payment_mollie_templates.xml',
        'views/account_move_view.xml',
        'views/account_payment_register.xml',
        'wizard/payment_capture_wizard_views.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'payment_mollie_official/static/src/js/payment_form.js',
            'payment_mollie_official/static/src/js/qr_dialog.js',
            'payment_mollie_official/static/src/scss/payment_form.scss',
            'payment_mollie_official/static/src/xml/dialog.xml',
        ]
    },

    'images': [
        'static/description/cover.png',
    ],
}
