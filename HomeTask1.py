from datetime import datetime, date

def get_days_from_today(string_date):
    try:
        return (datetime.strptime(string_date, "%Y-%m-%d").date() - date.today()).days
    except ValueError:
        return None

string_date = "2026-03-14"

print(get_days_from_today(string_date))
