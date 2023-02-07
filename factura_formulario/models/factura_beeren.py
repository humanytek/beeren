from odoo import fields, models

class Producto(models.Model):
    _inherit = ['product.template']

    Asin = fields.Char(
        related ='product_id.Asin',
        string= 'Asin',
    )