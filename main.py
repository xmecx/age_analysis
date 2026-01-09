ages = []

while True:
    user_input = input("Введи вік (0 — стоп): ")

    try:
        age = int(user_input)
    except ValueError:
        print("Будь ласка, введи число")
        continue

    if age < 0:
        print("Вік не може бути відʼємним")
        continue

    if age == 0:
        break

    ages.append(age)


if len(ages) == 0:
    print("Немає даних для аналізу")
else:
    total_people = len(ages)
    total_age = sum(ages)
    average_age = total_age / total_people

    count_adult = 0
    for age in ages:
        if age >= 18:
            count_adult += 1

    min_age = min(ages)
    max_age = max(ages)

    print("\nРезультати аналізу:")
print("Кількість людей:", total_people)
print("Мінімальний вік:", min_age)
print("Максимальний вік:", max_age)
print("Середній вік:", average_age)
print("Кількість повнолітніх:", count_adult)

if average_age >= 21:
    print("Аудиторія доросла")
else:
    print("Аудиторія молода")

