from openerp import models, fields, api
from datetime import timedelta,time,date,datetime

class enrollStudent(models.Model):
    _name = 'enroll.student'
    
    
    student_id = fields.Char('Student id')
    name = fields.Char('Fullname')
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
    
    teacher = fields.Many2one('hr.employee', string='Teacher')
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
        first = vals['first_name'].upper().strip()
        mid = vals['middle_name'].upper().strip()
        last = vals['last_name'].upper().strip()
        
        vals['name'] = first + ' ' + mid[0]+'.' + ' ' + last
        
        vals['student_id'] = self.env['ir.sequence'].get('stud_id') 
        
        return super(enrollStudent, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('first_name') :
            vals['first_name'] = vals.get('first_name').upper().strip()
        else:
            if self.first_name != False:
                vals['first_name'] = self.first_name.upper().strip()
                
        if vals.get('middle_name') :
            vals['middle_name'] = vals.get('middle_name').upper().strip()
        else:
            if self.middle_name != False:
                vals['middle_name'] = self.middle_name.upper().strip()
                
        if vals.get('last_name') :
            vals['last_name'] = vals.get('last_name').upper().strip()
        else:
            if self.last_name != False:
                vals['last_name'] = self.last_name.upper().strip()
                
        return super(enrollStudent, self).write(vals)   
  
                    
