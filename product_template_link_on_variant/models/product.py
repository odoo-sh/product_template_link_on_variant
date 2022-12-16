# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_view_product_template_form(self):
        action = self.env["ir.actions.actions"]._for_xml_id("sale.product_template_action")
        form_view = [(self.env.ref('product.product_template_only_form_view').id, 'form')]
        action['res_id'] = self.product_tmpl_id.id
        action['views'] = form_view
        return action
