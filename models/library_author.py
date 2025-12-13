from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Autor de Libro'

    name = fields.Char(string='Nombre Completo', required=True)
    biography = fields.Text(string='Biografía')