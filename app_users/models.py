from django.db import models

STATE_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SE", "Sergipe"),
    ("SP", "São Paulo"),
    ("TO", "Tocantins"),
)


# Create your models here.
class Reader(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100, verbose_name="Senha")

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")

    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Cidade")
    state = models.CharField(choices=STATE_CHOICES, max_length=2, null=True, blank=True, verbose_name="Estado")

    register_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de Registro")

    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Imagem de Perfil")

    def __str__(self) -> str:
        return f"{self.name} [{self.username}]"


class Author(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100, verbose_name="Senha")

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome")
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de Nascimento")

    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Cidade")
    state = models.CharField(choices=STATE_CHOICES, max_length=2, null=True, blank=True, verbose_name="Estado")

    register_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de Registro")

    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Imagem de Perfil")

    def __str__(self) -> str:
        return f"{self.name} [{self.username}]"


class Editor(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100, verbose_name="Senha")

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome")
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de Nascimento")

    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Cidade")
    state = models.CharField(choices=STATE_CHOICES, max_length=2, null=True, blank=True, verbose_name="Estado")

    register_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de Registro")

    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Imagem de Perfil")

    def __str__(self) -> str:
        return f"{self.name} [{self.username}]"
