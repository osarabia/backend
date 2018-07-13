from datetime import datetime
from decimal import Decimal

def convertToDate(value):
    try:
        dt = datetime.strptime(value, '%Y-%m-%d %H:%M')
    except Exception:
        return None, False

    return dt, True

def convertToDecimal(value):
    try:
        dc = Decimal(value)
    except Exception:
        return None, False

    return dc, True
