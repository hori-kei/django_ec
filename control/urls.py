from basicauth.decorators import basic_auth_required
from django.urls import path

from .views import (
    ManageListView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
)

app_name = "control"

urlpatterns = [
    path("products/", basic_auth_required(ManageListView.as_view()), name="manage_list"),
    path(
        "products/create/", basic_auth_required(ProductCreateView.as_view()), name="manage_create"
    ),
    path(
        "products/<int:pk>/edit/",
        basic_auth_required(ProductUpdateView.as_view()),
        name="manage_edit",
    ),
    path(
        "products/<int:pk>/delete/",
        basic_auth_required(ProductDeleteView.as_view()),
        name="manage_delete",
    ),
]
