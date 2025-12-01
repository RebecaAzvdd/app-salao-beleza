from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.nome_cliente} - {self.produto.nome}"