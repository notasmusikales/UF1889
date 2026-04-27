from odoo import models, fields


class Tutoring(models.Model):
    _name = 'academy.tutoring'
    _description = 'Tutoring Session'

    subject = fields.Char(string='Subject', required=True)
    session_date = fields.Datetime(string='Date', default=fields.Datetime.now)
    notes = fields.Text(string='Notes')
    student_id = fields.Many2one('academy.student', string='Student', required=True)
    active = fields.Boolean(string='Active', default=True)