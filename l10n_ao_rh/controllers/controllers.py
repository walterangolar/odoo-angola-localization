# -*- coding: utf-8 -*-
# from odoo import http


# class L10nAoRh(http.Controller):
#     @http.route('/l10n_ao_rh/l10n_ao_rh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ao_rh/l10n_ao_rh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ao_rh.listing', {
#             'root': '/l10n_ao_rh/l10n_ao_rh',
#             'objects': http.request.env['l10n_ao_rh.l10n_ao_rh'].search([]),
#         })

#     @http.route('/l10n_ao_rh/l10n_ao_rh/objects/<model("l10n_ao_rh.l10n_ao_rh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ao_rh.object', {
#             'object': obj
#         })

