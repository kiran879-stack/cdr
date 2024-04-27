from datetime import datetime
from .models import CDR

def parse_cdr_text_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 10:
                msisdn, imsi, imei, plan, call_type, corresp_type, corresp_isdn, duration_str, time_str, date_str = parts
                try:
                    duration = int(duration_str)
                    time = datetime.strptime(time_str, "%H:%M").time()
                    date = datetime.strptime(date_str, "%d/%m/%Y").date()
                    cdr_obj = CDR(
                        MSISDN=msisdn,
                        IMSI=imsi,
                        IMEI=imei,
                        PLAN=plan,
                        CALL_TYPE=call_type,
                        CORRESP_TYPE=corresp_type,
                        CORRESP_ISDN=corresp_isdn,
                        DURATION=duration,
                        TIME=time,
                        DATE=date
                    )
                    cdr_obj.save()
                except (ValueError, IndexError, TypeError) as e:
                    print(f"Error parsing line: {line}. {e}")
            else:
                print(f"Ignoring line due to incorrect format: {line}")

def match_cdrs_with_customers():
    cdrs = CDR.objects.all()
    for cdr in cdrs:
        try:
            customer = Customer.objects.get(MSISDN=cdr.MSISDN)
            cdr.customer = customer
            cdr.save()
        except Customer.DoesNotExist:
            print(f"No matching customer found for MSISDN: {cdr.MSISDN}")
