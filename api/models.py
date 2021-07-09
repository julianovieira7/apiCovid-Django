from django.db import models

class Estado(models.Model):
    def __init__(self, sigla, numeroCasos, recuperados, vacinados, numeroMortos):
        self.sigla = sigla
        self.numeroCasos = numeroCasos
        self.recuperados = recuperados
        self.vacinados = vacinados
        self.numeroMortos = numeroMortos



    sigla = models.CharField(max_length=20)
    numeroCasos = models.IntegerField
    recuperados = models.IntegerField
    vacinados = models.IntegerField
    numeroMortos = models.IntegerField

    def __repr__(self):
        return self.sigla + ", " + str(self.numeroCasos) + ", " + str(self.recuperados) + ", " + str(self.vacinados) + ", " + str(self.numeroMortos)