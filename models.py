#-*- coding utf-8 -*-

from openerp import fields, models

class Especies(models.Model):
    _name = 'examen.especies'
    
    name = fields.Char(string="Especie", required=True)
    
    