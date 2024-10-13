# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class l10n_ao_rh_contract_salary(models.Model):
#     _name = 'l10n_ao_rh_contract_salary.l10n_ao_rh_contract_salary'
#     _description = 'l10n_ao_rh_contract_salary.l10n_ao_rh_contract_salary'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

