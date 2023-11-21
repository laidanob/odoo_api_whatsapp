{
    'name': 'Odoo Api Whatsapp',
    'version': '14.0',
    'description': 'Odoo Send Template Message by Web Api Whatsapp',
    'summary': 'Odoo Send Api Whatsapp',
    'author': 'Bruno Laidano',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/send_message_wizard_view.xml',
        'views/sale_order.xml',
        
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}