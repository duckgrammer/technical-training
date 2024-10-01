from odoo import fields, models

class ResUsers(models.Models):
    _inherit = "res.users"
    property_ids = fields.One2many("estate.property", domain=[('state', 'is in', ['new','recieved'])])