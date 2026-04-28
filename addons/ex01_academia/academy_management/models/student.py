from odoo import models, fields, api

class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('graduated', 'Graduated'),
        ('dropped', 'Dropped')
    ], string='State', default='draft')

    tutoring_ids = fields.One2many(
        'academy.tutoring',
        'student_id',
        string='Tutorings'
    )

    tutoring_count = fields.Integer(
        string='Tutoring Count',
        compute='_compute_tutoring_count',
        store=True
    )

    last_tutoring_date = fields.Date(
        string='Last Tutoring Date',
        compute='_compute_last_tutoring_date',
        store=True
    )

    @api.depends('tutoring_ids')
    def _compute_tutoring_count(self):
        for record in self:
            record.tutoring_count = len(record.tutoring_ids)

    @api.depends('tutoring_ids.date')
    def _compute_last_tutoring_date(self):
        for record in self:
            if record.tutoring_ids:
                dates = record.tutoring_ids.mapped('date')
                record.last_tutoring_date = max(dates) if dates else False
            else:
                record.last_tutoring_date = False