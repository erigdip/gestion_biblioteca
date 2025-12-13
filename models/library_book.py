from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    name = fields.Char(string='Título del Libro', required=True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Activo', default=True)
    
    state = fields.Selection(
        selection=[
            ('available', 'Disponible'),
            ('borrowed', 'Prestado'),
            ('lost', 'Perdido')
        ],
        string='Estado',
        default='available'
    )

    description = fields.Text(string='Sinopsis')

    author_id = fields.Many2one('library.author', string='Autor')
    borrower_id = fields.Many2one('res.partner', string='Prestado a')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state != 'borrowed':
            self.borrower_id = False