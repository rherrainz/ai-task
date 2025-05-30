from django.views.generic import ListView, DetailView
from . import models

class ProductView(ListView):
    model = models.Product
    template_name = 'views/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'views/product_detail.html'
    context_object_name = 'product'

    