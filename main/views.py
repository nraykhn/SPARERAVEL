from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'nama_app' : 'SPARERAVEL',
        'npm' : '2306275701',
        'name': 'Nur Alya Khairina',
        'class': 'PBP A',
        'product_entries' : product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

# Untuk Menampilkan Data Berbentuk XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Untuk Menampilkan Data Berbentuk JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Untuk Menampilkan Data Berbentuk XML with ID
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")