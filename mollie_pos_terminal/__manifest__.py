{
    'name': 'Mollie Pos Terminal',
    'version': '18.0.0.1',
    'description': '',
    'summary': 'Connect your pos with mollie terminal',
    'author': 'Mollie',
    'maintainer': 'Droggol Infotech Private Limited',
    'license': 'LGPL-3',
    'category': 'Point of Sale',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mollie_pos_terminal_views.xml',
        'views/mollie_pos_terminal_payments_views.xml',
        'views/res_config_settings_views.xml',
        'views/pos_payment_method_views.xml',
        'wizard/mollie_sync_terminal.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'mollie_pos_terminal/static/**/*',
        ],
    },
    'images': [
        'static/description/cover.png',
    ],
}

# after payment cancel create new line with mollie throw error 'payment in progress'
