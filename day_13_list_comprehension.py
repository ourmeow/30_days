

def filter_numbers():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    filtered_num = [i for i in numbers if i > 0]
    print(filtered_num)

filter_numbers()

def flatten_num():
    list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten = [number for row in list_of_lists for number in row]
    print(flatten)
flatten_num()

def list_of_tuples():
    tuples = [([i] + [i ** j for j in range(6)] ) for i in range(11) ]
    for tuple in tuples:
        print(tuple, "\n")

list_of_tuples()

def flatten_dic():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    flatten = [{'country': country[0].upper(),'city': country[1].upper()} for row in countries for country in row]
    for country in flatten:
        print(country, "\n")
flatten_dic()

def conc_strings():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    conc = [[first+' '+ last] for row in names for first,last in row]
    
    print(conc)
conc_strings()