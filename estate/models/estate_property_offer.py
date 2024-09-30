from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "tag estate property offers"

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'),('refused','Refused')],copy=False)
    partner_id = fields.Many2one("res.partner",required=True)
    property_id = fields.Many2one("estate.property", required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_valid_date", inverse="_inverse_valid")

    @api.depends("validity", "create_date")
    def _valid_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Date.today(), days=record.validity)

    def _inverse_valid(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.to_date(record.create_date)).days
            