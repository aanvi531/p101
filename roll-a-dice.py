import random
response = input("Do you want to roll a dice? ")
response = str("y") 

while response == "y":
    no = random.randint(1,6)
    if no:
        print(no)
    elif response == str("n"):
        break
        


