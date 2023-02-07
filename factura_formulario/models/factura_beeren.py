from odoo import fields, models


class factura_beeren(models.Model):
    _inherit = "product.template"

    Asin = fields.Char(
        related ='product_id.Asin',
        string= 'Asin',
    )
