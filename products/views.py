# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Product


class ProductList(ListView): 
    model = Product

class ProductDetail(DetailView): 
    model = Product

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Cadastro realizado com sucesso!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Atualização concluída com sucesso!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Deletado com sucesso!"


