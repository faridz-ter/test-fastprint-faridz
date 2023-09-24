from django.db import models
from utils.models import CreateUpdate

# Create your models here.

class Kategori(CreateUpdate):
    nama_kategori = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_kategori
class Status(CreateUpdate):
    nama_status = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_status
class Produk(CreateUpdate):
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_produk