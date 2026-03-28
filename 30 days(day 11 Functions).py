#ex8
def ex8(list:list):
    for i in list:
        print(list)


#ex9
def reverse_list(list:list):
    reversed_list = []

    for e in list[len(list)-1::-1]:
        reversed_list.append(e)
    return reversed_list

#ex10 
def capitalize_list_items(list:list):
    capital_list = []
    for i in list:
        capital_list.append(i.capitalize())
        
    return capital_list
food_stuff = ['Potato', 'tomato', 'Mango', 'Milk']

#ex11
def add_item(list:list,item):
    list.append(item)
    return list


#ex12
def remove_item(list:list, item):
    list.remove(item)
    return list

#ex13
def sum_of_numbers(number):
    res = 0
    for i in range(1,number+1):
        res+=i
    return res

#ex16
def evens_odds(number:int):
    even = 0
    odd = 0
    for i in range(0,number+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

#ex17
def factorial(number):
    res = 1
    for i in range(number,0,-1):
        res *= i
    return res

#ex18

