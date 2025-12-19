from django.urls import path

from .views import ManageListView, ProductCreateView

app_name = "control"

urlpatterns = [
    path("products/", ManageListView.as_view(), name="manage_list"),
    path("products/create/", ProductCreateView.as_view(), name="manage_create"),
]
