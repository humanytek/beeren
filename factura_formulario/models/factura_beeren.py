from odoo import fields, models

class Producto(models.Model):

  Asin = fields.Char(
    related ="product_id.Asin",
    string= "Asin",
  )