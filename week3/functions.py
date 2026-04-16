# def great_user(name):
#     print(f"Hello {name}")


# great_user("Mike")
# great_user('Joe')

# def calculate_tax(salary):
#     computed_tax_charge= (salary*0.2)
#     return computed_tax_charge

# tax_value1=calculate_tax(500000)
# print(f"The tax payments for this month is {tax_value1}")

# def introduce_yourself(name,age):
#     print(f"I'm {name}. I am {age} years old.")

# introduce_yourself("Alex",24) #Position argument.
# introduce_yourself(24,"Alex")
# introduce_yourself(24,"Alex") #Keyword arguments
# #Default parameters
def greet_user(name="Guest",age=0,phone="+25678787686",email="defaultemail@cutsocare.com"):
    print(f"Hello, {name}. How are you doing today?")
    print(f"You are {age} years old.")

# greet_user(name="Jones",age=34)
# greet_user(age=12)
    
# def add_item(item,items=[]):
#     items.append(item)
#     return items

# print(add_item("Pen"))
# print(add_item("Book"))
# print(add_item("Calculator"))
# def add_item(item,items=None):
#     if items is None:
#         items=[]
#     items.append(item)
#     return items

# print(add_item("Pen"))
# print(add_item("Book"))
# print(add_item("Calculator"))

#Variable arguments
# def calculate_total_marks(*scores):
#     return sum(scores)

# print(calculate_total_marks(98,87,67,46,98))

# def compute_average_scores(*scores):
#     return sum(scores)/len(scores)

# print(f"The average score is {compute_average_scores(98,67,87,93)}")

#Keyword variable arguments:

# def show_profile(**info):
#     for key,value in info.items():
#         print(f"{key}:{value}")

# show_profile(name="Mike",age=24)

#Combining Position arguments,positional variable arguments and keyword variable arguments
# def combined_demo(a,b,c,d,*numbers,**profile):
#     print({a,b,c,d})
#     print(sum(numbers))
#     for key,value in profile.items():
#         print(f"{key}: {value}")
# combined_demo(2,3,4,4,5,5,8,8,name="Joel",age=37,country="Uganda")


#Unpacking variable arguments

# def add_numbers(a,b,c):
#     return a+b+c
# numbers=[45,12,32]


# print(add_numbers(*numbers))
# print(add_numbers(45,12,32))

#return values:
# def compute_square_root(number):
#     return number**0.5

# result1=compute_square_root(4)
# print(f"Result of computation is {result1}")
# def compute_square(number):
#     return number*number

# print(f"Result of computation is {compute_square(7)}")

#Returning multiple values
# def quotient_and_remainder(x,y):
    
#     return x//y ,x%y

# quotient,remainder=quotient_and_remainder(100,8)
# print(f"The result is: Quotient:{quotient} and remainder is {remainder}")

#Variable scopes
counter=7 # Global scope
def modify_counter(number):
    counter=5 #Local scope.
    return counter+number
print(modify_counter(6))

print(counter+8)
    

#Nested Function
def multiply_numbers(a,b,c):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
        c (_type_): _description_
    """
    def multiply(a,b):
        d=6
        return a*b*d
    return c* multiply(a,b)
print(multiply_numbers(2,3,4))