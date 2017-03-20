from openerp import models, fields, api

class employee(models.Model):
    _inherit = 'hr.employee'
    
    firstname = fields.Char(string="First Name", size=128)
    middlename = fields.Char(string="Middle Name", size=128)
    lastname = fields.Char(string="Last Name", size=128)
    fullname = fields.Char('Fullname', readonly=True)
    
    @api.model
    def create(self, vals):
        first = vals['firstname'].upper().strip()
        mid = vals['middlename'].upper().strip()
        last = vals['lastname'].upper().strip()
        
        vals['name'] = first + ' ' + mid[0]+'.' + ' ' + last
                
        return super(employee, self).create(vals)
