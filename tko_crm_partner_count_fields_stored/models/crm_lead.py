# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2017 ThinkOpen Solutions (<https://tkobr.com>).
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class Lead(models.Model):
    _inherit = 'crm.lead'

    calendar_event_ids = fields.One2many('calendar.event', 'opportunity_id',
                                         domain="[('res_model', '=', 'res.partner')]", string='Messages')
    meeting_count = fields.Integer('# Meetings', compute='_compute_meeting_count', stored=True)

    @api.multi
    @api.depends('calendar_event_ids')
    def _compute_meeting_count(self):
        return super(Lead, self)._compute_meeting_count()
