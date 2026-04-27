from odoo import models, fields


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    specialty = fields.Char(string='Specialty')
    active = fields.Boolean(string='Active', default=True)

    course_ids = fields.One2many('academy.course', 'instructor_id', string='Courses')
    tutoring_ids = fields.One2many('academy.tutoring', 'teacher_id', string='Tutoring Sessions')