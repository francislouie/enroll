# -*- coding: utf-8 -*-
from openerp import http

# class EnrollmentMain(http.Controller):
#     @http.route('/enrollment_main/enrollment_main/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enrollment_main/enrollment_main/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enrollment_main.listing', {
#             'root': '/enrollment_main/enrollment_main',
#             'objects': http.request.env['enrollment_main.enrollment_main'].search([]),
#         })

#     @http.route('/enrollment_main/enrollment_main/objects/<model("enrollment_main.enrollment_main"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enrollment_main.object', {
#             'object': obj
#         })