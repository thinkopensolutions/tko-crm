# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api
 

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_company = fields.Boolean(related='partner_id.is_company')
    email = fields.Char(string='Email', related='partner_id.email')
    phone = fields.Char(string='Phone', related='partner_id.phone')
    mobile = fields.Char(string='Mobile', related='partner_id.mobile')
    partner_mobile = fields.Char(string='Mobile', related='partner_id.mobile')
    poc_id = fields.Many2one('res.partner', string='Point of Contact', related='partner_id.poc_id')
    poc_email = fields.Char(string='Point of Contact Email', related='poc_id.email')
    poc_mobile = fields.Char(string='Point of Contact Mobile', related='poc_id.mobile')


    @api.model
    def create(self, vals):
        res = super(CrmLead, self).create(vals)
        if res.partner_id and vals.get('poc_id'):
            child_ids = [x.id for x in res.partner_id.child_ids]
            if vals.get('poc_id') not in  child_ids:
                res.poc_id.write({'parent_id':res.partner_id.id})
        return res

    @api.multi
    def write(self, vals):
        res = super(CrmLead, self).write(vals)
        for oppo in self:
            if not vals.get('partner_id') or vals.get('poc_id'):
                child_ids = [x.id for x in self.partner_id.child_ids]
                if  vals.get('poc_id') not in child_ids:
                     # self.env['res.partner'].browse(vals.get('poc_id')).write({'parent_id':self.partner_id.id})
                     self.poc_id.write({'parent_id':self.partner_id.id})
        return res
