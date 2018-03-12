# -*-coding:utf-8-*-
from odoo import models, fields


class CRM(models.Model):
    _inherit = 'crm.lead'

    lost_reason_info = fields.Char(string=u'More info')
