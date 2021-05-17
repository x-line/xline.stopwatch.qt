from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def business_days(today = datetime.today()):
    """
    Returns number of business days in month of date passed in, or today (default)
    """
    start_filter = datetime(today.year, today.month, 1) # 1st of the month
    end_filter = start_filter + relativedelta(months=1) # 1st of next month
    start_filter -= relativedelta(days=1)               # Last day of prev month
    end_filter -= relativedelta(days=1)               # Last day of this month
    daygenerator = (start_filter + timedelta(x + 1) for x in range((end_filter - start_filter).days))
    business_days = sum(1 for day in daygenerator if day.weekday() < 5)
    return business_days

def business_days_mtd(today = datetime.today()):
    """
    Counts business days in month, up to and including date passed in.
    Defaults to today (default)
    """
    start_filter = datetime(today.year, today.month, 1) # 1st of the month
    end_filter = start_filter + relativedelta(months=1) # 1st of next month
    start_filter -= relativedelta(days=1)               # Last day of prev month
    end_filter -= relativedelta(days=1)               # Last day of this month
    daygenerator = (start_filter + timedelta(x + 1) for x in range((end_filter - start_filter).days))
    business_days = 0
    for day in daygenerator:
        if day.weekday() < 5 and day.day <= today.day:
            business_days += 1
        # print(f'{day}, {day.weekday() < 5 and day.day <= today.day}, {day.weekday() < 5}, {day.day <= today.day}, {business_days}')

    # business_days = sum(1 for day in daygenerator if day.weekday() < 5 and day.day <= today.day)
    return business_days

# We could really do with a test for this file.