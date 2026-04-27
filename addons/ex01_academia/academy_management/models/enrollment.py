from odoo import models, fields


class Enrollment(models.Model):
    _name = 'academy.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('academy.student', string='Student', required=True)
    course_id = fields.Many2one('academy.course', string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_enrollment', 'unique(student_id, course_id)', 'Student already enrolled in this course!')
    ]