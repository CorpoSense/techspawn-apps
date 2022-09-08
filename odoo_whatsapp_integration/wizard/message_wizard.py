from odoo import models, fields

class MessageError(models.TransientModel):
    _name='display.error.message'

    def get_message(self):
        if self.env.context.get("message", False):
            return self.env.context.get('message')
        return False

    name = fields.Text(string="Message", readonly=True, default=get_message)

