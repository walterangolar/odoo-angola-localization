# -*- coding: utf-8 -*-
# from odoo import http


# class L10nAo(http.Controller):
#     @http.route('/l10n_ao/l10n_ao', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ao/l10n_ao/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ao.listing', {
#             'root': '/l10n_ao/l10n_ao',
#             'objects': http.request.env['l10n_ao.l10n_ao'].search([]),
#         })

#     @http.route('/l10n_ao/l10n_ao/objects/<model("l10n_ao.l10n_ao"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ao.object', {
#             'object': obj
#         })

