# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    require_expected_date = fields.Boolean(
        string='Require Expected Closing',
        help='If checked, the Expected Closing date will be required '
             'for opportunities that enter this stage.',
    )
