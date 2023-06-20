from django.shortcuts import get_object_or_404, render

from .forms import ProductForm
from .models import Product


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    product_list = Product.objects.all()
    context = {"product_list": product_list, "form": ProductForm()}
    return render(request, "tracker/index.html", context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "tracker/detail.html", {"product": product})
