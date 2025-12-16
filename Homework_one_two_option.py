from datetime import datetime, date

def get_days_from_today(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = date.today()
        return (input_date - today).days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте YYYY-MM-DD")


user_date = input("Введіть дату у форматі YYYY-MM-DD: ")

try:
    days_difference = get_days_from_today(user_date)
    print(f"Кількість днів між сьогоднішньою датою та {user_date}: {days_difference}")
except ValueError as e:
    print(e)