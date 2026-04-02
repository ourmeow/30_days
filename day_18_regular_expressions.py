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


print("EXERSICE 1:")
for i in ex1():
    print(i)

#ex2
def ex2():
    points = ['-12', '-4', '-3', '-1', '0', '4', '8']
    regex_pattern = r'-?\d+'
    found_points = [int(num) for num in points]

    sorted_points = sorted(found_points)
    distance = max(sorted_points) - min(sorted_points)
    print(sorted_points)
    return distance
print("EXERSICE 2:", ex2())

#ex3 
def ex3(text):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern,text))

print("EXERSICE 3:", ex3('firstname'))

#ex4
def ex4():
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
    found_list = re.findall(r'[^a-zA-Z\s]',sentence)
    result = []
    for i in found_list:
        if i in result:
            result[0] += 1
        else: 
            result[0] = 1
            result[1] = i
    result.sort(reverse=True)
    return result
print("EXERSICE 4:", ex4())