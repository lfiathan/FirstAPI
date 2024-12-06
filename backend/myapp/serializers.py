from rest_framework import serializers
from .models import Karyawan, Departemen, Jabatan, Absensi, Gaji

class DepartemenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departemen
        fields = '__all__'

class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = '__all__'

class KaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = '__all__'

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = '__all__'

class GajiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gaji
        fields = '__all__'

