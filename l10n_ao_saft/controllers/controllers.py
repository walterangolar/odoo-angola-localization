# -*- coding: utf-8 -*-
# from odoo import http


# class L10nAoSaft(http.Controller):
#     @http.route('/l10n_ao_saft/l10n_ao_saft', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ao_saft/l10n_ao_saft/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ao_saft.listing', {
#             'root': '/l10n_ao_saft/l10n_ao_saft',
#             'objects': http.request.env['l10n_ao_saft.l10n_ao_saft'].search([]),
#         })

#     @http.route('/l10n_ao_saft/l10n_ao_saft/objects/<model("l10n_ao_saft.l10n_ao_saft"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ao_saft.object', {
#             'object': obj
#         })

