
from django.urls import path
from .views import (
    KaryawanListCreateView,
    KaryawanDetailView,
    DepartemenListCreateView,
    DepartemenDetailView,
    JabatanListCreateView,
    JabatanDetailView,
    AbsensiListCreateView,
    AbsensiDetailView,
    GajiListCreateView,
    GajiDetailView,
)

urlpatterns = [
    path('karyawan/', KaryawanListCreateView.as_view(), name='karyawan-list-create'),
    path('karyawan/<int:pk>/', KaryawanDetailView.as_view(), name='karyawan-detail'),
    path('departemen/', DepartemenListCreateView.as_view(), name='departemen-list-create'),
    path('departemen/<int:pk>/', DepartemenDetailView.as_view(), name='departemen-detail'),
    path('jabatan/', JabatanListCreateView.as_view(), name='jabatan-list-create'),
    path('jabatan/<int:pk>/', JabatanDetailView.as_view(), name='jabatan-detail'),
    path('absensi/', AbsensiListCreateView.as_view(), name='absensi-list-create'),
    path('absensi/<int:pk>/', AbsensiDetailView.as_view(), name='absensi-detail'),
    path('gaji/', GajiListCreateView.as_view(), name='gaji-list-create'),
    path('gaji/<int:pk>/', GajiDetailView.as_view(), name='gaji-detail'),
]

