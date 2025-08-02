from odoo import models, fields, api

class QuickdeskTicket(models.Model):
    _name = 'quickdesk.ticket'
    _description = 'Support Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Subject", required=True, tracking=True)
    description = fields.Text(string="Description", required=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, string="Created By")
    agent_id = fields.Many2one('res.users', string="Assigned Agent")
    category_id = fields.Many2one('quickdesk.category', string="Category")
    attachment = fields.Binary(string="Attachment")
    status = fields.Selection([
        ('open', 'Open'),
        ('progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ], default='open', tracking=True)
    upvotes = fields.Integer(default=0)
    downvotes = fields.Integer(default=0)

    def action_upvote(self):
        self.upvotes += 1

    def action_downvote(self):
        self.downvotes += 1
