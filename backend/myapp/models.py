from django.db import models

# Create your models here.
class Departemen(models.Model):
    nama_departemen = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_departemen

class Jabatan(models.Model):
    nama_jabatan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_jabatan

class Karyawan(models.Model):
    STATUS_CHOICES = [
        ('aktif','Aktif'),
        ('nonaktif','Nonaktif'),
    ]

    nama_lengkap = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    tanggal_masuk = models.DateField(blank=True, null=True)
    departemen = models.ForeignKey(Departemen, on_delete=models.SET_NULL, null=True)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nama_lengkap


class Absensi(models.Model):
    STATUS_ABSENSI_CHOICES = [
        ('hadir', 'Hadir'),
        ('izin', 'Izin'),
        ('sakit', 'Sakit'),
        ('alpha', 'Alpha'),
    ]

    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    waktu_masuk = models.TimeField(blank=True, null=True)
    waktu_keluar = models.TimeField(blank=True, null=True)
    status_absensi = models.CharField(max_length=10, choices=STATUS_ABSENSI_CHOICES)

    def __str__(self):
        return f"{self.karyawan.nama_lengkap} - {self.tanggal}"


class Gaji(models.Model):
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    bulan = models.CharField(max_length=10)
    gaji_pokok = models.DecimalField(max_digits=10, decimal_places=2)
    tunjangan = models.DecimalField(max_digits=10, decimal_places=2)
    potongan = models.DecimalField(max_digits=10, decimal_places=2)
    total_gaji = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.karyawan.nama_lengkap} - {self.bulan}"
