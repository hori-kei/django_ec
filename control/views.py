# Create your views here.
from django.http import HttpResponse


def product_list(request):
    return HttpResponse("control products list")
