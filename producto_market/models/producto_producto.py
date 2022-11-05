from odoo import fields, models

class Producto(models.Model):
  _inherit = "product.template"
  Asin = fields.Char(string="Asin",)
  