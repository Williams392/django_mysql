# Sirve para poder convertir los datos nativos que ORM me provee a un JSON y pueda devorvelos
# como respuesta a través de esta API con Django RestFramework.

# 3

from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

