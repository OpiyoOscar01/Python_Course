# We use while loops when a given condition is true or satisfied

# x=2
# while x<12:
#     print(f"{x**2}")
#     x=x+1
# else:
#     print("Loop execution completed successfully")
    
# while True:
#     print("-------Our Menu--------")
#     print("Select options:")
#     print("1. Hello, world")
#     print("2.Good bye!")
#     choice=input("Enter your choice: ")
#     if choice==1:
#         print("Hello world")
#         break
#     elif choice==2:
#         print("Good bye")
#         break
#     else:
#         print("Invalid choice")

while True:
    age=input("Enter your age: ")
    if age.isdigit():
        age=int(age)
        print(f"Your age, {age} has been recorded successfully")
        break
    else:
        print("Please enter a valid number")