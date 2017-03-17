from openerp import models, fields, api

class enrollsubject(models.Model):
    _name = 'enroll.subject'
    
    code = fields.Char('Code', readonly=True)
    description = fields.Char('Description')
    name = fields.Char('Name')
    
    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].get('subj_code')
        return super(enrollsubject, self).create(vals)