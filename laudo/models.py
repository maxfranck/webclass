from django.db import models

class Documento(models.Model):
    codigo = models.TextField()
    cultura = models.CharField(max_length=50)
    oferta_id = models.IntegerField()
    oferta = models.CharField(max_length=50)
    amostra_id = models.IntegerField()
    produtor = models.CharField(max_length=150)
    distribuidor = models.CharField(max_length=150)
    rts = models.CharField(max_length=150)
    ats = models.CharField(max_length=150)

    def __str__(self):
        return str(self.amostra_id)