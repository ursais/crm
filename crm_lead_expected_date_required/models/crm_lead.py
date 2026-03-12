# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    stage_require_expected_date = fields.Boolean(
        related='stage_id.require_expected_date',
        readonly=True,
    )

    @api.multi
    def write(self, vals):
        result = super(CrmLead, self).write(vals)
        if 'stage_id' in vals:
            new_stage = self.env['crm.stage'].browse(vals['stage_id'])
            if new_stage.require_expected_date:
                leads_missing = self.filtered(lambda l: not l.date_deadline)
                if leads_missing:
                    raise ValidationError(_(
                        'The Expected Closing date is required when moving '
                        'to the "%s" stage. Please set the Expected Closing '
                        'date before proceeding.'
                    ) % new_stage.name)
        return result
