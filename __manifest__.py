# -*- coding: utf-8 -*-
{
    'name': "sonderp",
    'summary': """Demo o aplicación de prueba presentado por sonderp_ para su negocio""",
    'description': """ Gestion de procesos de venta, compra, facturación e inventario para su negocio """,
    'author': "Sonderp_ ",
    'website': "http://www.sonderp.com",
    'category': 'Operations',
    'version': '13.0',
    'depends': ['base'],
    'data': [
        # 'security/security.xml'
        'security/ir.model.access.csv',
        'views/view_menus.xml',
        'views/view_buy.xml',
        'views/view_supplier.xml',
        'views/view_category.xml',
        'views/view_stock.xml',
        'views/view_tax.xml',
        'views/view_bill_buy.xml',
        'views/view_bill_sell.xml',
        'views/view_client.xml',
        'views/view_price.xml',
        'views/view_sell.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
