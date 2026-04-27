from odoo import models, fields


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    duration = fields.Integer(string='Duration (hours)')
    price = fields.Float(string='Price')
    active = fields.Boolean(string='Active', default=True)

    instructor_id = fields.Many2one('res.partner', string='Instructor')
    enrollment_ids = fields.One2many('academy.enrollment', 'course_id', string='Enrollments')