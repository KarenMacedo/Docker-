# -*- coding: utf-8 -*-
from odoo import models, fields, api

class biblioteca_categoria(models.Model):

    _name = 'biblioteca.categoria'
    id = fields.Char(string='Id')
    name = fields.Char(string='Genero', required=True)
    description = fields.Text('Descripcion')




