from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import html2text
import urllib.parse as parse


class SendWhatsappMessageWizaes(models.TransientModel):
    _name = 'send.whatsapp.wizard'
    _description = 'Send Whatsapp Message Wizard'
    sale_order = fields.Many2one('sale.order', string="Order")
    phone_number = fields.Char(related='sale_order.partner_id.mobile')
    phone_code = fields.Integer(related='sale_order.partner_id.country_id.phone_code', string='Phone Code')
    template_email = fields.Many2one('mail.template', string='Template')
    body_text = fields.Text('Text to send')
    send_number = fields.Char(string='Phone Number',  compute='_compute_send_number')
    
    @api.onchange('sale_order')
    def update_phone_number(self):
        self._compute_send_number()
         
    @api.onchange('template_email')
    def template_html(self):
        print(self.phone_number)
        template = self.template_email
        if template:
            values = template.generate_email(self.sale_order.id, ['body_html'])
            self.body_text = html2text.html2text(values.get('body_html'))
        
        return 
     
    def _compute_send_number(self):
        self.send_number = (f'{self.phone_code}{self.phone_number}')
        
    def send_message(self):
        # If the text is sent via URL, we need to transform it into a valid URL.
        if not self.body_text:
            raise ValidationError(_('There are no message'))  
        
        body_text = parse.quote(self.body_text)
        phone_number = self.phone_number
        phone_code = self.phone_code
        
        url = f"https://web.whatsapp.com/send?phone={phone_code}{phone_number}&text={body_text}"
        
        if (not phone_number or phone_code == 0):
            raise ValidationError(_(f'''The phone code or the phone number are no valid
                                    Phone Code is:{phone_code}
                                    Phone Number is:{phone_number}'''))
         
        else:      
            send_msg = {
                    'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new',
                }
            return send_msg
        
        