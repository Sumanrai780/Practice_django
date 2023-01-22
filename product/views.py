from django.shortcuts import render, reverse 
from django.http import HttpResponseRedirect 
from product.forms import ProductForm

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")

def product_list(request):
    return render(request, "product_list.html")

def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("product:product_list"))
    context = {"form": form}
    return render(request, "form.html", context)
