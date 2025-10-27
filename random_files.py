import random

n = random.randint(1, 10)  
print(f"Случайно избран брой файлове: {n}")

for i in range(1, n + 1):
    filename = f"random_file_{i}.txt"
    f = open(filename, "w")
    f.write(f"Това е файл номер {i} от общо {n}\n")
    f.close()
    print(f"Създаден файл: {filename}")