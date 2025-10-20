from django.db import models

# Create your models here.
class Apresentacao(models.Model):
    nome = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='apresentacao/')
    link_contato = models.URLField(default="#")

    def __str__(self):
        return self.nome


class Skill(models.Model):
    categoria = models.CharField(max_length=100)  # Ex: Linguagens, Frameworks
    habilidades = models.TextField(help_text="Liste as habilidades separadas por vírgula.")
    
    def __str__(self):
        return self.categoria


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='apresentacao/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Certificado(models.Model):
    emissor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    competencias = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.emissor}"


class SobreMim(models.Model):
    titulo = models.CharField(max_length=200, default="Sobre mim")
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='apresentacao/')
    def __str__(self):
        return "Sobre mim"
