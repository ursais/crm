# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'CRM Lead Expected Date Required',
    'version': '10.0.1.0.0',
    'category': 'Customer Relationship Management',
    'summary': 'Require Expected Closing date on configurable CRM stages',
    'author': 'Open Source Integrators',
    'website': 'https://www.opensourceintegrators.com',
    'license': 'AGPL-3',
    'depends': [
        'crm',
    ],
    'data': [
        'views/crm_stage_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
}
