input_file = "input.txt"
output_file = "output.txt"

f = open(input_file, "r")
lines = f.readlines()
odd_lines = [line for index, line in enumerate(lines) if index % 2 == 0]
f.close()

f = open(output_file, "w")
f.writelines(odd_lines)
f.close()

print(f"Новият файл - {output_file} - съдържа само нечетните редове.")
