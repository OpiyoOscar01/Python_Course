numbers=[2,3,4,5,6,7,8,9]

for number in numbers:
    if number%3==0:
        break
    print(number,end=" ")
print(" ")
# Using continue statement
for number in numbers:
    if number%3==0:
        continue
    print(number,end=" ")
for number in numbers:
    pass
