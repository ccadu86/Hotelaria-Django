from django.db import models

# Create your models here.
class homepage(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    logo = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return self.titulo
    

class quarto(models.Model):

    tipo_quarto = [
        ("Solteiro", "Solteiro"),
        ("Premium", "Premium"),
        ("Plus", "Plus"),
    ]
    status_status = [
        (1, "Disponivel"),
        (0, "Reservado")
    ]

    num_Quarto = models.IntegerField()
    qtd_Hospedes = models.IntegerField()
    tipo = models.CharField(choices=tipo_quarto)
    valor = models.FloatField(max_length=3)
    descricao = models.TextField(max_length=300)
    status = models.BooleanField(choices=status_status, default=1)
    img = models.ImageField(upload_to='quarto/')
