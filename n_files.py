# Задача 1: Генериране на n файла
n = int(input("Въведи колко файла да се създадат: "))

for i in range(1, n + 1):
    filename = f"file_{i}.txt"
    f = open(filename, "w")
    f.write(f"Това е съдържанието на файл номер {i}\n")
    f.close()
    print(f"Създаден файл: {filename}")
