# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	po_released_person = fields.Many2one('res.users', string='Issued by', index=True, track_visibility='onchange', default=lambda self: self.env.user)

