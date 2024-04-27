from django.http import HttpResponse
from .utils import parse_cdr_text_file
from .utils import match_cdrs_with_customers
from rest_framework import generics
from .models import CDR
from .serializers import CDRSerializer

def parse_cdr_and_insert(request):
    cdr_file_path = './customer.txt'
    parse_cdr_text_file(cdr_file_path)
    return HttpResponse("CDR file parsed and inserted into the database.")

def match_cdrs_and_customers(request):
    match_cdrs_with_customers()
    return HttpResponse("CDRs matched with customers.")

class CDRListAPIView(generics.ListAPIView):
    queryset = CDR.objects.all()
    serializer_class = CDRSerializer