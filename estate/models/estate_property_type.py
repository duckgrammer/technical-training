from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "group estate property by type"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_type', 'UNIQUE(name)',
         'The name must be unique.'),
    ]