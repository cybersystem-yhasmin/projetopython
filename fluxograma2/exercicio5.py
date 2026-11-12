a = 90000000
b = 140000000
anos = 0

while a <= b:
    a = a * 1.035
    b = b * 1.01
    anos += 1

print("Anos necessários:", anos)
print("População do país A:", a)
print("População do país B:", b)