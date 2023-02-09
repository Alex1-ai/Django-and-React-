from rest_framework import serializers
from .models import SupportStaff


class SupportStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupportStaff
        fields = [
            'info', 'name', 'phone', 'whatsapp'

        ]
