filename = "contacts.txt"

while True:
    print("1. Додати новий контакт")
    print("2. Переглянути список контактів")
    print("3. Вийти")

    choice = int(input("Ваш вибір: "))

    if choice == 1:
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        email = input("Введіть електронну пошту: ")

        with open(filename, "a") as file:
            file.write(f"Ім'я: {name}, Телефон: {phone}, Електронна пошта: {email}\n")
        print("Контакт додано успішно!")

    elif choice == 2:
        with open(filename, "r") as file:
            print("Список контактів:" if file else "Контакти відсутні.")
            print(file.read())

    elif choice == 3:
        print("Програма завершена.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
