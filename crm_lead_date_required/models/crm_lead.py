# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    stage_require_expected_date = fields.Boolean(
        related='stage_id.require_expected_date',
        readonly=True,
    )

    @api.constrains('stage_id', 'date_deadline')
    def _check_date_deadline_required(self):
        for lead in self:
            if (lead.stage_id.require_expected_date
                    and not lead.date_deadline):
                raise ValidationError(
                    'The "Expected Closing" date is required '
                    'for opportunities in the "%s" stage.'
                    % lead.stage_id.name
                )
