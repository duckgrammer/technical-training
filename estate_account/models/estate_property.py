from odoo import models

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_property(self):
        return super().sold_property()