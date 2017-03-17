from openerp import models, fields, api
from datetime import timedelta,time,date,datetime

class enrollStudent(models.Model):
    _name = 'enroll.student'
  
    student_id = fields.Char('Student id',readonly=True)
    fullname = fields.Char('Fullname', readonly=True)
    first_name = fields.Char('First Name', required=True, size=128)
    middle_name = fields.Char('Middle Name', required=True, size=128)
    last_name = fields.Char('Last Name', required=True, size=128)    
    nick_name = fields.Char('Nick Name')
    
    age_complete = fields.Char(compute='_get_age',string='Age')
    age = fields.Char(compute='_get_age',store = True)
    
    birthplace = fields.Char('Birth Place')
    birth_date = fields.Date('Birth Date', required=True)
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], required=True)
    photo = fields.Binary('Photo')
    height = fields.Float('Height')
    weight = fields.Float('Weight')
    religion = fields.Char('Religion')
    citizen = fields.Char('Citizen')
    
    subject = fields.Many2many('enroll.subject',string='Subject')
    
    @api.depends('birth_date')
    def _get_age(self):
        for r in self:
            if r.birth_date:
                bdate = datetime.strptime(r.birth_date,"%Y-%m-%d").date()
                today = date.today()
                diffdate = today - bdate

                years = diffdate.days/365
                formonth = diffdate.days - (years * 365.25)
                months = (formonth/31)
        
                bday = bdate.day
                tody = date.today().day
                
                if tody >= bday:
                    day = tody-bday
                else:
                    day = 31 - (bday-tody)
                
                r.age_complete = str(years) + ' Year/s ' + str(int(months)) + ' Month/s ' + str(day) + ' Day/s' 
                r.age = str(years)
    @api.model
    def create(self, vals):       
        first = vals['first_name']
        mid = vals['middle_name']
        last = vals['last_name']
        
        vals['fullname'] = first + ' ' + mid + ' ' + last
        
        vals['student_id'] = self.env['ir.sequence'].get('stud_id') 
        
        return super(enrollStudent, self).create(vals)


# class parent_father(models.Model):
#     _name = 'parent.father'
#         
#     first_name = fields.Char('First Name', required=True, size=128)
#     middle_name = fields.Char('Middle Name', required=True, size=128)
#     last_name = fields.Char('Last Name', required=True, size=128)
#     religion = fields.Char('Religion')
#     citizen = fields.Char('Citizen')
#     photo = fields.Binary('Photo')
#     birth_date = fields.Date('Birth Date', required=True)
#     address = fields.Char('Permanent Address')    
#     
# class parent_mother(models.Model):    
#     _name = 'parent.mother'
#     
#     first_name = fields.Char('First Name', required=True, size=128)
#     middle_name = fields.Char('Middle Name', required=True, size=128)
#     last_name = fields.Char('Last Name', required=True, size=128)    
#     religion = fields.Char('Religion')
#     citizen = fields.Char('Citizen')
#     photo = fields.Binary('Photo')
#     birth_date = fields.Date('Birth Date', required=True)
#     address = fields.Char('Permanent Address')