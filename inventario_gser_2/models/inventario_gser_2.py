from odoo import fields, models


class inventario_gser_2 (models.Model):
    _inherit = "stock.move.line"

    folio_1 = fields.Char(
        string= 'Folio',
    )
