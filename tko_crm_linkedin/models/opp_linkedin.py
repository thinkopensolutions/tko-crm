# -*-coding:utf-8-*-
from odoo import models, fields


class Linkedin_Opp(models.Model):
    _inherit = 'crm.lead'
    linkedin = fields.Char('Linkedin', related='partner_id.linkedin')


class Linkedin_Partner(models.Model):
    _inherit = 'res.partner'
    linkedin = fields.Char('Linkedin')
