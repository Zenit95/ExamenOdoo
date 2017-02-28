#-*- coding utf-8 -*-

from openerp import fields, models, api

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
    destruido = fields.Boolean(default=False)
    fecha_destruccion = fields.Date()
    
class Jedi(models.Model):
    _name = 'examen.servivo'
    _inherit ='examen.servivo'
    
    color_sable = fields.Selection([
        ('azul', "Azul"),
        ('verde', "Verde"),
        ('morado', "Morado"),
    ])
    ultima_vista = fields.Date()
    planeta = fields.Many2one('examen.planeta', string="Planeta", required=True)
    midiclorianos = fields.Integer()
    nivel = fields.Char(string="Nivel", compute='_calc_nivel')
    
    @api.depends('midiclorianos')
    def _calc_nivel(self):
        for r in self:
            if r.midiclorianos < 100:
                r.nivel = "Padawan"
            elif r.midiclorianos > 100 and r.midiclorianos < 1000:
                r.nivel = "Caballero Jedi"
            else:
                r.nivel = "Consejero Jedi"
    