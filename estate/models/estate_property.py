from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property table"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Integer()
    bedrooms = fields.Integer(default=2)
    garden = fields.Boolean()
    garden_orientation = fields.Selection([("north", "North"),("east", "East"),("south", "South"),("west", "West")])
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    availibility_date = fields.Date(copy=False, default=fields.Date.add(fields.Date.today(), months=3))
    
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([("new", "New"),("received","Offer Received"),("accepted","Offer Accepted"),("sold","Sold"),("cancel","Cancelled")], required=True, copy=False, default="new")