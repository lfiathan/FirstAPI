from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Departemen, Jabatan, Karyawan, Absensi, Gaji

admin.site.register(Departemen)
admin.site.register(Jabatan)
admin.site.register(Karyawan)
admin.site.register(Absensi)
admin.site.register(Gaji)

