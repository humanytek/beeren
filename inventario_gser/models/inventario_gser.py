from odoo import fields, models


class inventario_gser (models.Model):
    _inherit = "stock.move.line"

    folio = fields.Char(
        string= 'Folio',
    )

    folio_1 = fields.Char(
        string= 'Folio',
    )
