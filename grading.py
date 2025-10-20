grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good  = []
passing = []
fail = []

def print_lists(list):
    for i in list:
        print(i)

# excellent → оценки >= 90
# good → оценки от 70 до 89
# pass → оценки от 50 до 69
# fail → оценки под 50

for i in grades:
    if i >= 90:
        excellent.append(i)
    elif i > 69 and i < 90:
        good.append(i)
    elif i >= 50 and i < 70:
        passing.append(i)
    elif  i < 50:
        fail.append(i)
        
print("Excellent grades:")
print_lists(excellent)
print("Good grades:")
print_lists(good)
print("Passing students:")
print_lists(passing)
print("Failing grades:")
print_lists(fail)
        