from odoo import models, fields, api


class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    birth_date = fields.Date(string='Birth Date')
    active = fields.Boolean(string='Active', default=True)

    tutoring_ids = fields.One2many('academy.tutoring', 'student_id', string='Tutoring Sessions')

    tutoring_count = fields.Integer(string='Total Tutoring Sessions', compute='_compute_tutoring_count', store=True)
    last_tutoring_date = fields.Datetime(string='Last Tutoring Session', compute='_compute_last_tutoring', store=True)
    academic_state = fields.Selection([
        ('good', 'Good'),
        ('regular', 'Regular'),
        ('poor', 'Needs Improvement'),
    ], string='Academic Status', default='good')

    @api.depends('tutoring_ids')
    def _compute_tutoring_count(self):
        for record in self:
            record.tutoring_count = len(record.tutoring_ids)

    @api.depends('tutoring_ids.session_date')
    def _compute_last_tutoring(self):
        for record in self:
            if record.tutoring_ids:
                last_session = max(record.tutoring_ids.mapped('session_date'))
                record.last_tutoring_date = last_session
            else:
                record.last_tutoring_date = False