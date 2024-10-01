from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_property(self):
        vals_list = []
        for record in self:
            print(record.buyer)
            vals_list.append({
                "partner_id": record.buyer.id,
                "move_type": "out_invoice",
                "line_ids": [
                    Command.create({
                        "name": record.name+" invoice 6%",
                        "quantity": 1,
                        "price_unit": record.selling_price*0.06,
                    }),
                    Command.create({
                        "name": "administrative fees",
                        "quantity": 1,
                        "price_unit": 100,
                    })
                ],
            })
        self.env["account.move"].create(vals_list)

        return super().sold_property()