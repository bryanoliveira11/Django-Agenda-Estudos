from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoria')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Criação')
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    
    def __str__(self) -> str:
        return f'{self.first_name}'
    
    class Meta():
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'