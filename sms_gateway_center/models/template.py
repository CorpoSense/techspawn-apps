from openerp import models, api, _, fields


class template_sms(models.Model):
    _name = 'template.sms'
    _description = 'SMS Templates'

    name = fields.Char(String='Template Name', required=False)

    sms_content = fields.Text(String='sms_content', required=False)
