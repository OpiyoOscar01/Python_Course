squares=[]
for number in range(10):
    squares.append(number**2)
print(squares)

# List comprehension way:
print([x**3 for x in range(9)])

even_numbers=[y for y in range(2,20) if y%2==0]

print(even_numbers)