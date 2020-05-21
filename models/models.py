# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sonderp_1(models.Model):
#     _name = 'sonderp_1.sonderp_1'
#     _description = 'sonderp_1.sonderp_1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
