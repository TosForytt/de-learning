from datetime import date

people = [
    {"name": "Анна", "birth_year": 2000},
    {"name": "Игорь", "birth_year": 1995},
    {"name": "Мария", "birth_year": 2010},
    {"name": "Алексей", "birth_year": 1988},
    {"name": "Ольга", "birth_year": 2023}
]

def calculate_age(birth_year):
    """Возвращает возраст относительно текущего года."""
    current_year = date.today().year
    return current_year - birth_year

def age_word(age):
    """Возвращает правильное склонение слова (год, года, лет)."""
    if 11 <= age % 100 <= 19:
        return "лет"
    
    remainder = age % 10
    if remainder == 1:
        return "год"
    elif remainder in (2, 3, 4):
        return "года"
    else:
        return "лет"

print("--- Список людей ---")
for person in people:
    age = calculate_age(person["birth_year"])
    word = age_word(age)
    print(f"{person['name']}, {age} {word}.")

print("\n--- Проверка подбора слова ---")
test_ages = [1, 2, 5, 11, 21, 22, 25]
for test_age in test_ages:
    word = age_word(test_age)
    print(f"{test_age} {word}")