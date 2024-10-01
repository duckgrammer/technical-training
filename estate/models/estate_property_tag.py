from odoo import fields, models

class EstatePropertyTypeTag(models.Model):
    _name = "estate.property.tag"
    _description = "tag estate properties"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_tag', 'UNIQUE(name)',
         'The name must be unique.'),
    ]