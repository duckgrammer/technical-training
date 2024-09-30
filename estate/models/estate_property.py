from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property table"

    name = fields.Char(required=True)
    expected_price = fields.Float(required=True)

    selling_price = fields.Float(readonly=True, copy=False)
    availibility_date = fields.Date(copy=False)