from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status, generics
from rest_framework.response import Response
from .models import Karyawan, Departemen, Jabatan, Absensi, Gaji
from .serializers import KaryawanSerializer, DepartemenSerializer, JabatanSerializer, AbsensiSerializer, GajiSerializer

# Departemen Views
class DepartemenListCreateView(generics.ListCreateAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer

    def delete(self, request, *args, **kwargs):
        Departemen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            file = request.data['file']
            data = json.load(file)
            for item in data:
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

class DepartemenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer
    lookup_field = "pk"

# Jabatan Views
class JabatanListCreateView(generics.ListCreateAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer

    def delete(self, request, *args, **kwargs):
        Departemen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        # Handle JSON file upload
        if request.data.get('file'):
            file = request.data['file']
            data = json.load(file)
            for item in data:
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

class JabatanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    lookup_field = "pk"

# Karyawan Views
class KaryawanListCreateView(generics.ListCreateAPIView):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer

    def delete(self, request, *args, **kwargs):
        Departemen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            file = request.data['file']
            data = json.load(file)
            for item in data:
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

class KaryawanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer
    lookup_field = "pk"

# Absensi Views
class AbsensiListCreateView(generics.ListCreateAPIView):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer

    def delete(self, request, *args, **kwargs):
        Departemen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            file = request.data['file']
            data = json.load(file)
            for item in data:
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

class AbsensiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer
    lookup_field = "pk"

# Gaji Views
class GajiListCreateView(generics.ListCreateAPIView):
    queryset = Gaji.objects.all()
    serializer_class = GajiSerializer

    def delete(self, request, *args, **kwargs):
        Departemen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            file = request.data['file']
            data = json.load(file)
            for item in data:
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

class GajiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gaji.objects.all()
    serializer_class = GajiSerializer
    lookup_field = "pk"


