from rest_framework import serializers
from .models import CDR

class CDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CDR
        fields = ['id', 'MSISDN', 'IMSI', 'IMEI', 'PLAN', 'CALL_TYPE', 'CORRESP_TYPE', 'CORRESP_ISDN', 'DURATION', 'TIME', 'DATE']