from openerp import models, fields, api

class parent_guardian(models.Model):
    _name = 'parent.guardian'
         
    firstname = fields.Char('First Name', required=True, size=128)
    middlename = fields.Char('Middle Name', required=True, size=128)
    lastname = fields.Char('Last Name', required=True, size=128)
    religion = fields.Char('Religion')
    citizen = fields.Char('Citizen')
    photo = fields.Binary('Photo')
    birth_date = fields.Date('Birth Date', required=True)
    address = fields.Char('Permanent Address')
    contact_number = fields.Char('Contact Information')
    
    student_ids = fields.Many2many('enroll.student', string='Student(s)')

class enrollStudent(models.Model):
    _inherit = 'enroll.student'
    
    parent_ids = fields.Many2many('parent.guardian', string='Parent')