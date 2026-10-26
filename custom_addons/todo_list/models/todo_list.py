from odoo import models, fields, api
from odoo.exceptions import ValidationError

# ไว้เก็บ tags
class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    name = fields.Char(string='Tag Name', required=True)

# ตัวหลัก Todo List
class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List Module'

    name = fields.Char(string='Title', required=True)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    # เช็ค End Date > Start Date
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("Start Date must be before End Date.")
            
    attendee_ids = fields.Many2many('res.users', string='Attendees')

    line_ids = fields.One2many('todo.list.line', 'todo_id', string='Lines')

    state = fields.Selection([
        ('draft', 'DRAFT'),
        ('in_progress', 'IN PROGRESS'),
        ('complete', 'COMPLETE')
    ], string='Status', default='draft', tracking=True)

    def action_in_progress(self):
        self.state = 'in_progress'

    def action_complete(self):
        for record in self:
            if any(not line.is_complete for line in record.line_ids):
                raise ValidationError("All lines must be checked off before the status can be changed to complete.")
        record.state = 'complete'

class TodoListLine(models.Model):
    _name = 'todo.list.line'
    _description = 'Todo List Line'

    todo_id = fields.Many2one('todo.list', string='Todo Reference', ondelete='cascade')
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    is_complete = fields.Boolean(string='Is Complete', default=False)