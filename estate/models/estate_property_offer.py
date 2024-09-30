from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "tag estate property offers"

    name = fields.Char(required=True)