from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk
from .forms import ProdukForm  # Anda perlu membuat formulir untuk edit dan tambah

def produk_list(request):
    produk_list = Produk.objects.all()
    return render(request, 'produk_list.html', {'produk_list': produk_list})

def produk_filter(request):
    produk_filter = Produk.objects.filter(status__nama_status='bisa dijual')
    return render(request, 'produk_filter.html', {'produk_filter': produk_filter})

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'tambah_produk.html', {'form': form})

def edit_produk(request, id_produk):
    produk = get_object_or_404(Produk, id=id_produk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'edit_produk.html', {'form': form, 'produk': produk})

def hapus_produk(request, id_produk):
    produk = get_object_or_404(Produk, id=id_produk)
    if request.method == 'POST':
        produk.delete()
        return redirect('produk_list')
    return render(request, 'hapus_produk.html', {'produk': produk})