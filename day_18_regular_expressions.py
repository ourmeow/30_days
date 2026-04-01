import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

#ex1
def ex1():
    sub_string = re.sub(r'\.','', paragraph)
    words_list = re.split(' ', sub_string)
    result = []
    for i in words_list:
        found = False
        for j in result:
            if i == j[1]:
                j[0] += 1
                found = True
        if not found:
            result.append([1,i])
    
    result.sort(reverse=True)
    return result
    
print("EXERSICE 1: ")
for i in ex1():
    print(i)
    
                    
