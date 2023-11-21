from odoo import models, _

class WhatsappSaleOrder(models.Model):
    _inherit = "sale.order"
    
    def action_whatsapp(self):
        action = self.env.ref('odoo_api_whatsapp.send_whatsapp_action').read()[0]
        return action
