from odoo import fields, models


class inventario_gser_2 (models.Model):
    _inherit = "stock.move.line"

    x_studio_folio_opd = fields.Char(
        string= 'Folio OPD',
    )
    x_studio_folio_o = fields.Char(
        string= 'Folio O',
    )
