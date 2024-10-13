# -*- coding: utf-8 -*-
# from odoo import http


# class L10nAoRhContractSalary(http.Controller):
#     @http.route('/l10n_ao_rh_contract_salary/l10n_ao_rh_contract_salary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ao_rh_contract_salary/l10n_ao_rh_contract_salary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ao_rh_contract_salary.listing', {
#             'root': '/l10n_ao_rh_contract_salary/l10n_ao_rh_contract_salary',
#             'objects': http.request.env['l10n_ao_rh_contract_salary.l10n_ao_rh_contract_salary'].search([]),
#         })

#     @http.route('/l10n_ao_rh_contract_salary/l10n_ao_rh_contract_salary/objects/<model("l10n_ao_rh_contract_salary.l10n_ao_rh_contract_salary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ao_rh_contract_salary.object', {
#             'object': obj
#         })

