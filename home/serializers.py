from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id', 'first_name', 'last_name', 'blood_group', 'Donated_date', 'phone', 'age', 'address', 'volume_donated']

        #fields = ['__all__']