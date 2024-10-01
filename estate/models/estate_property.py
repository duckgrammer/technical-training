from odoo import _,api,fields, models
from odoo.exceptions import UserError

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

    property_type_id = fields.Many2one("estate.property.type", String="Property Type")
    property_tag_id = fields.Many2many("estate.property.tag", String="Property Tag")
    property_offer_id = fields.One2many("estate.property.offer", "property_id", String="Offer")

    buyer = fields.Many2one("res.partner")
    salesperson = fields.Many2one("res.users", default=lambda self: self.env.user)

    living_area = fields.Float()
    garden_area = fields.Float()
    total_area = fields.Float(compute="_compute_area")

    @api.depends("garden_area", "living_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    best_price = fields.Float(compute="_max_offer")

    @api.depends("property_offer_id.price")
    def _max_offer(self):
        for record in self:
            if record.property_offer_id:
                record.best_price = sum(record.property_offer_id.mapped('price'))
            else:
                record.best_price=0

    @api.onchange("garden")
    def _north_garden_area(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def cancel_property(self):
        if self.state != "sold":
            self.state = "cancel"
        else:
            raise UserError(_('I sold property can\'t be cancelled'))

    def sold_property(self):
        if self.state != "cancel":
            self.state = "sold"
        else:
            raise UserError(_('I canclled property can\'t be sold'))