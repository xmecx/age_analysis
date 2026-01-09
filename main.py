ages = []

while True:
    age = int(input("Введи вік (0 — стоп): "))
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

    print("Мінімальний вік:", min_age)
    print("Максимальний вік:", max_age)
    print("Кількість повнолітніх:", count_adult)
    print("Середній вік:", average_age)

    if average_age >= 21:
        print("Аудиторія доросла")
    else:
        print("Аудиторія молода")