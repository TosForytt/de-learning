from datetime import date
name = "Анна"
birth_year = 2000
current_year = date.today().year
age = current_year - birth_year
print(f"Меня зовут {name}, мне {age} год")