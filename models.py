#-*- coding utf-8 -*-

from openerp import fields, models

class Especie(models.Model):
    _name = 'examen.especie'
    
    name = fields.Char(string="Especie", required=True)
    
class SerVivo(models.Model):
    _name = 'examen.servivo'
    
    especie_id = fields.Many2one('examen.especies',
            string="Especie")
    
class Planeta(models.Model):
    _name = 'examen.planeta'
    
    name = fields.Char(string="Planeta", required=True)
    distancia = fields.Integer();
    existe = fields.Boolean(default=False)
    fechaDestruccion = fields.Date()
    