from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from product.models import Product


class ManageListView(ListView):
    model = Product
    template_name = "control/manage_list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "price", "image"]
    template_name = "control/manage_create.html"
    success_url = reverse_lazy("control:manage_list")
