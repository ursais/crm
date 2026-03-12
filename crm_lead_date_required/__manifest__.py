# -*- coding: utf-8 -*-
# Copyright 2026 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Lead Expected Date Requirement",
    "summary": "Allow requiring Expected Closing date on specific CRM stages",
    "version": "10.0.1.0.0",
    "category": "Customer Relationship Management",
    "author": "Open Source Integrators, "
              "Odoo Community Association (OCA)",
    "website": "https://www.opensourceintegrators.com",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "crm",
    ],
    "data": [
        "views/crm_stage_views.xml",
        "views/crm_lead_views.xml",
    ],
}
