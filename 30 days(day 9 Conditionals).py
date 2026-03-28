#1 
def ex1():
    user_input = int(input("enter your age: "))
    if user_input >= 18:
        print("you are old enough to drive")
    else: 
        print("you are not old enough to drive") 
        
#ex2
def ex2():
    user_input = int(input("Enter your age: "))
    if user_input > 10:
        user_input2 = user_input - 10
        if user_input2 > 1:
            print(f"You are {user_input2} years older than me")
        else:
            print(f"You are {user_input2} year older than me")
    else:
        print("You cant be useing this app")

#ex3
def ex3():
    input_1 = int(input("Enter number 1: "))
    input_2 = int(input("Enter number 2: "))
    if input_1 > input_2:
        print(f"Number {input_1} is bigger than {input_2}")
    elif input_2 > input_1:
        print(f"Number {input_2} is bigger than {input_1}")
    else:
        print("They are equal")

#ex4
def ex4():
    score = int(input("Enter the score:"))
    if score >= 90 and score <= 100:
        print("A")
    elif  score >= 80 and score <= 89:
        print("B")   
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    elif score <= 59 and score >= 0:
        print("F")
    
def ex5():
    month = input("Enter a month")
    if month == "September" or month == "October" or month == "November":
        print("Its Autumn")
    elif month == "December" or month == "January" or month == "February":
        print("Winter")
    elif month == "March" or month == "April" or month == "May":
        print("Spring")
    elif month == "June" or month == "July" or month == "August":
        print("Summer")

def ex6():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    add_fruit = input("Enter a fruit: ")
    if add_fruit in fruits:
        print('That fruit already exist in the list')
    else:
        fruits.append(add_fruit)
        print(f"{add_fruit} was added to the list")

def ex7():
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
    if "skills" in person:
        print(person["skills"][2])
        if "Python" in person["skills"]:
            print("Yes")
    if "JavaScript" in person["skills"] and "React" in person["skills"] and "Node" not in person["skills"] and "MongoDB" not in person["skills"] and "Python" not in person["skills"]:
        print('He is a front end developer')
    if person["is_married"] == True:
        print(f"{person['first_name']} {person['last_name']} lives in {person["country"]}. He is married")
ex7()