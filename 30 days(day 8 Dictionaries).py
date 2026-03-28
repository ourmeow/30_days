dog = {}
dog['name'] = 'Violet'
dog['color'] = 'Blue'
dog['breed'] = 'Labrador'
dog['legs'] = '4'
dog['age'] = '5'

student = {
    'first_name':"Kiborg",
    "last_name":"Hikora",
    "gender":"MALE",
    "age":23,
    "marital_status":True,
    "skills": ["python","SQL","killing"],
    "country":"Ukraine",
    "city":"Odessa",
    "address":"Lev Tolst 5"
}

print(len(student))
data = type(student["skills"])
print(data)
student["skills"].append("New Skill")
print(student["skills"])

print(student.items())
student.pop("address")
print(student)