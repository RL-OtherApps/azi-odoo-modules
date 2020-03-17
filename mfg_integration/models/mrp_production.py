# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.production'

    routing_detail = fields.Char(
        string="Routing Detail",
        compute='_compute_routing_detail',
        store=True)

    @api.depends('routing_id')
    def _compute_routing_detail(self):
        for mo in self:
            if mo.routing_id:
                work_center_codes = [code for code in mo.routing_id.operation_ids.mapped('workcenter_id.code') if code]
                mo.routing_detail = ", ".join(work_center_codes)
