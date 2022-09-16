from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"


class ProductView(DetailView):
    model = Product
    template_name = "products/detail_view.html"


class CreateProduct(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "products/create_product.html"

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.add_product")


class UpdateProduct(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/update_product.html"
    permission_required = "webapp.change_product"

    # def has_permission(self, **kwargs):
    #     return self.request.user.has_perm("webapp.change_product")


class DeleteProduct(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "products/delete_product.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = "webapp.delete_product"
