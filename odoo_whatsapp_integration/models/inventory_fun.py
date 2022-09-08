from odoo import models, fields, api

import urllib.parse as parse

class InventoryTransferDone(models.Model):
    _inherit = 'stock.picking'

    def action_whatsapp(self):
        prods = ""
        for rec in self:
            for id in rec.move_lines:
                prods = prods + "*" +str(id.product_id.name) + " : " + str(id.quantity_done) + "* \n"


        record_phone = self.partner_id.mobile
        custom_msg = "Hello *{}*, your order *{}* is shipped.\n The items shipped are as follows: \n{}".format(str(self.partner_id.name),str(self.name),prods)

        if not record_phone:
            view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = "Please add a mobile number!"
            return{
                'name':'Mobile Number Field Empty',
                'type':'ir.actions.act_window',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'display.error.message',
                'views':[(view.id,'form')],
                'view_id': view.id,
                'target':'new',
                'context':context
            }

        if record_phone[0] == "+":

            ph_no = [number for number in record_phone if number.isnumeric()]
            ph_no = "".join(ph_no)
            ph_no = "+" + ph_no
            if 10 <= len(ph_no) <= 14:

                link = "https://web.whatsapp.com/send?phone=" + ph_no
                message_string = parse.quote(custom_msg)
                url_id = link + "&text=" + message_string
                return {
                    'type':'ir.actions.act_url',
                    'url': url_id,
                    'target':'new',
                    'res_id': self.id,
                }

            else:
                view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = "Mobile number does not exists. Please add a valid mobile number!"
                return {
                    'name': 'Invalid Mobile Number',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'display.error.message',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context
                }
        else:
            view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = "No Country Code! Please add a valid mobile number along with country code!"
            return {
                'name': 'Invalid Mobile Number',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'display.error.message',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context
            }
