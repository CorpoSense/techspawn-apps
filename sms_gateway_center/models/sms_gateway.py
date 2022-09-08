import time
from openerp import models, api, _, fields
import urllib
import twilio
from twilio.rest import Client
from openerp.exceptions import except_orm, Warning, RedirectWarning


class customer_sms(models.Model):
    _name = 'customer.sms'
    _description = 'Send SMS'

    select_template = fields.Boolean(
        String="Use Predefined Template", default=False)

    state = fields.Selection(
        [('draft', 'Draft'), ('sent', 'Send'), ('resend', 'Resend'), ], default='draft')

    templates = fields.Many2one('template.sms', 'Template Name', default=None)
    multi_customer = fields.Many2many(
        comodel_name='res.partner', String='Select Multiple customers')

    to_number = fields.Char(String="Send To", required=False)
    text = fields.Text(String="Message", required=False)
    select_account = fields.Many2many(
        comodel_name='api.configure', String="Account Info", required=True)

    @api.onchange('templates')
    def onchange_template(self):
        if self.select_template == True:
            self.text = self.templates.sms_content
        else:
            self.text = None

    @api.onchange('select_template')
    def onchange_account(self):

        if self.select_template == False:
            self.templates = self.select_template
            self.text = self.text

    @api.model
    def create(self, vals):
        res = super(customer_sms, self).create(vals)
        return res

    @api.multi
    def submit_bulk(self, ids):

        boolean=False
        if self.text:
            self.state = 'sent'
            msg = self.text
            select_account = self.select_account
            for acc in select_account:
                for tw_cust in self.multi_customer:
                    if acc.gateway_name == 'twilio':
                        client = Client(acc.sid, acc.auth_key)
                        try:
                            message = client.messages.create(
                                body=msg, to=tw_cust.mobile, from_=acc.from_no)
                        except:
                            if tw_cust.mobile is boolean:
                                raise Warning("Mobile Number is Not Available   ")
                            else:    
                                raise Warning("To number: "+tw_cust.mobile+" is Incorrect a mobile number")
                            
                else:
                    if self.multi_customer:
                        for cust in self.multi_customer:
                            if cust.mobile:
                                # Your authentication key.
                                authkey = acc.auth_key
                                # Multiple mobiles numbers separated by comma.
                                mobiles = cust.mobile
                                message = msg  # Your message to send.
                                # Sender ID,While using route4 sender id should
                                # be 6 characters long.
                                sender = acc.sender_id_msg91
                                route = "template"  # Define route
                                # Prepare you post parameters
                                values = {
                                    'authkey': authkey,
                                    'mobiles': mobiles,
                                    'message': message,
                                    'sender': sender,
                                    'route': route
                                }
                                # API URL
                                url = "http://api.msg91.com/api/sendhttp.php"
                                # URL encoding the data here.
                                postdata = urllib.parse.urlencode(
                                    values).encode("utf-8")
                                req = urllib.request.Request(url, postdata)
                                response = urllib.request.urlopen(req)
                                output = response.read()  # Get Response
                    else:
                        raise Warning("PLEASE SELECT CUSTOMERS")


class api_configure(models.Model):

    _name = 'api.configure'

    gateway_name = fields.Selection(
        [('twilio', 'Twilio'), ('msg_91', 'MSG91')], String='Select Gateway', required=True, store=True, default='twilio')
    name = fields.Char(String='Sms Gateway Name', required=True, store=True)
    sid = fields.Char(String='Sender Id')
    auth_key = fields.Char(String='User Authentication key', required=True)
    from_no = fields.Char(String='From Number')
    sender_id_msg91 = fields.Char(String="Msg91 Sender ID")

    @api.multi
    def submit_values(self):
        val = {}
        return {'name': self.name,
                'sid': self.sid,
                'auth_key': self.auth_key,
                'from_no': self.from_no

                }

    @api.model
    def create(self, vals):

        if vals['gateway_name'] == 'msg_91':

            if vals['sender_id_msg91'] == False:
                raise Warning('Sender Id is required')
            elif len(vals['sender_id_msg91']) > 6 or len(vals['sender_id_msg91']) < 6:
                raise Warning('Sender Id must be 6 chracter long is required')
        else:
            if vals['gateway_name'] == 'twilio' and vals['sid'] == False:
                raise Warning('Sid is Required')
            elif vals['gateway_name'] == 'twilio' and vals['from_no'] == False:
                raise Warning('From Number is Required')

        rec = super(api_configure, self).create(vals)
        return rec
