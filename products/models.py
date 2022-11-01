# -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    name = models.CharField('Tipo de quarto', max_length=100)
    description = models.TextField('Diária', blank=True)
    price = models.DecimalField('Preço do quarto', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Criado', auto_now_add=True)
    changed = models.DateTimeField('alterado', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
