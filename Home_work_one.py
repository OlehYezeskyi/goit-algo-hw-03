from datetime import datetime, date

def get_days_from_today(date_string):
    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = date.today()
        return (given_date - today).days
    except ValueError:
        raise ValueError("Date must be in format YYYY-MM-DD")
    
print(get_days_from_today("2020-10-09"))  
print(get_days_from_today("2025-01-01"))   


