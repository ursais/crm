# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    require_expected_date = fields.Boolean(
        string='Require Expected Closing',
        default=False,
        help='When enabled, opportunities moved to this stage must have '
             'the Expected Closing date set.',
    )
