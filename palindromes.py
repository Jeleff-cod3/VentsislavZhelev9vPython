words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)
        
for word in palindromes:
    print(word)