from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "tag estate property offers"

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'),('refused','Refused')],copy=False)
    partner_id = fields.Many2one(required=True)
    property_id = fields.Many2one(required=True)