# -*- coding: utf-8 -*-

from openerp import models, fields, api

class enrollreligion(models.Model):
    _name = 'enroll.religion'
    
    name = fields.Char(string='Religion')
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         'The religion must be unique')]
    
class enrollcitizen(models.Model):
    _name = 'enroll.citizen'
    
    name = fields.Char(string='Citizen')
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         'The citizen must be unique')]
