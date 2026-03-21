
# A    OPERATOR AND    RESULT
# T             T        T
# F             F        F
# F             T        F
# T             F        F
#Truth tables.
# IS_DRIVER=  False
# has_permit=True
# if IS_DRIVER or has_permit:
#     print("You are allowed to drive")
# else:
#     print("You can not drive")
    
    
# if not IS_DRIVER:
#     print("..........")

# word="apples"
# if "z" not in word:
#     print(f"Letter found in {word}")
# else:
#     print("Result not found")
    

fruits = ["apple", "banana", "cherry"]
search_keyword=input("Search for your favorite fruit: ").lower()
if search_keyword in fruits:
    print(f"{search_keyword} is in store.You can make an order")
else:
    print(f"Sorry, {search_keyword} is unavailable. Please check back later")  
     