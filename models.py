from django.db import models
class Customer(models.Model):
    customer_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    MSISDN = models.CharField(max_length=20)

class CDR(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    MSISDN = models.CharField(max_length=20)
    IMSI = models.CharField(max_length=20)
    IMEI = models.CharField(max_length=20)
    PLAN = models.CharField(max_length=100)
    CALL_TYPE = models.CharField(max_length=100)
    CORRESP_TYPE = models.CharField(max_length=100)
    CORRESP_ISDN = models.CharField(max_length=20)
    DURATION = models.IntegerField()
    TIME = models.TimeField()
    DATE = models.DateField()
