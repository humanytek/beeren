{
    'name': 'Pagos Beeren',
    'version': '15.0.0.1.0',
    'author': 'Fernando Rodriguez',
    'summary': 'Ajuste del formato de pago',
    'category': 'Accounting',
    'depends': [
        'account','product','producto_market'
    ],
    'data': [
        'views/pago_beeren.xml',
        'report/pagobeeren.xml',
    ],
    'installable': True,
    'auto_install': False,
}
