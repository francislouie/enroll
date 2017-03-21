from openerp import models, fields, api

class parent_guardian(models.Model):
    _name = 'parent.guardian'
         
    firstname = fields.Char('First Name', required=True, size=128)
    middlename = fields.Char('Middle Name', required=True, size=128)
    lastname = fields.Char('Last Name', required=True, size=128)
    religion_id = fields.Many2one('enroll.religion',string='Religion')
    citizen_id = fields.Many2one('enroll.citizen',string='Citizen')
    photo = fields.Binary('Photo')
    birth_date = fields.Date('Birth Date', required=True)
    address = fields.Char('Permanent Address')
    contact_number = fields.Char('Contact Information')
    
    student_ids = fields.Many2many('enroll.student', string='Student(s)')
    
    @api.one
    @api.constrains('birth_date')
    def _check_birthdate(self):
        if self.birth_date(self):
            raise ValidationError(_(
                "Birth Date can't be greater than current date!"))

class enrollStudent(models.Model):
    _inherit = 'enroll.student'
    
    parent_ids = fields.Many2many('parent.guardian', string='Parent')
    