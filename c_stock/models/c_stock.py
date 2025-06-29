
from odoo import fields, models

class c_stock(models.Model):
    _name = 'c.stock'
    _description = 'c_stock'
    
    
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    quantity = fields.Float(string='Quantity')
    product_id = fields.Many2one('product.product', string='Product')
    location_id = fields.Many2one('stock.location', string='Location')
    scrap_location_id = fields.Many2one('stock.location', string='Scrap Location')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done')],
        string='Status', default="draft", readonly=True, tracking=True)
    date_done = fields.Datetime('Date', readonly=True)
    
    
    def action_scrap(self):
        self.ensure_one()
          
    
    def action_validate(self):
        return
    
    def action_cancel(self):
        return