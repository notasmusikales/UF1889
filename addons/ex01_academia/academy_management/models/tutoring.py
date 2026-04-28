from odoo import models, fields, api

class AcademyTutoring(models.Model):
    _name = 'academy.tutoring'
    _description = 'Academy Tutoring'

    name = fields.Char(string='Subject', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    notes = fields.Text(string='Notes')

    student_id = fields.Many2one(
        'academy.student',
        string='Student',
        required=True,
        ondelete='cascade'
    )