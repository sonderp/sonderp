# -*- coding: utf-8 -*-
# from odoo import http


# class Sonderp1(http.Controller):
#     @http.route('/sonderp_1/sonderp_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sonderp_1/sonderp_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sonderp_1.listing', {
#             'root': '/sonderp_1/sonderp_1',
#             'objects': http.request.env['sonderp_1.sonderp_1'].search([]),
#         })

#     @http.route('/sonderp_1/sonderp_1/objects/<model("sonderp_1.sonderp_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sonderp_1.object', {
#             'object': obj
#         })
