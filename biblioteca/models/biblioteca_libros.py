# -*- coding: utf-8 -*-
from odoo import models, fields, api

class biblioteca_libro(models.Model):

    _name = 'biblioteca.libro'
    id = fields.Char(string = 'Id')
    name = fields.Char(string = 'Titulo', required = True)
    description = fields.Text('Descripcion')
    autor = fields.Text('Autor del libro')
    date = fields.Datetime(string='Fecha de registro')
    image = fields.Binary(string='imagen')
    categoria = fields.Many2one('biblioteca.categoria', string="Categoria", ondelete = 'restrict')


     # categoria = fields.One2many(comodel_name = 'biblioteca.categoria', inverse_name = 'name')


# textfield.htmlText
# https://emperove.gitbooks.io/fundamentos-de-desarrollo-odoo-10/content/
