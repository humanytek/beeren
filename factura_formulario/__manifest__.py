{
    'name': 'Factura Beeren',
    'version': '15.0.0.1.0',
    'author': 'Fernando Rodriguez',
    'summary': 'Module to hide Account field in Invoice Lines',
    'category': 'Accounting',
    'depends': [
        'account','product','producto_market'
    ],
    'data': [
        'views/factura_beeren.xml',
        'report/facturabeeren.xml',
    ],
    'installable': True,
    'auto_install': False,
}
