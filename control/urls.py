from django.urls import path

from .views import (  # ProductDeleteView,
    ManageListView,
    ProductCreateView,
    ProductUpdateView,
)

app_name = "control"

urlpatterns = [
    path("products/", ManageListView.as_view(), name="manage_list"),
    path("products/create/", ProductCreateView.as_view(), name="manage_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="manage_edit"),
    # path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="manage_delete"),
]
