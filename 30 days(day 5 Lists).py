empty_list = ()
list_with_5 = ["Lol","loler","give up","dont give up", "pretend"]
print(list_with_5[0], list_with_5[2], list_with_5[4])
mixed_data_types = ['Val', 24, 183,'not married','47 ronins']
it_companies = ['Facebook', 'Google', 'Microsoft', "Apple", 'IBM' , 'Oracle', "Amazon"]
print(it_companies)
print(it_companies.count("Facebook"))
it_companies.append('NewVal')
it_companies.insert(0,'FACEBOOK')
it_companies.remove('IBM')
it_companies.pop()
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_lists = front_end + back_end
joined_lists_copy = joined_lists.copy()
joined_lists_copy.insert(5,'Python')
joined_lists_copy.insert(6,'SQL')
print(joined_lists_copy)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max_age = max(ages)
min_age = min(ages)
print(min_age)
print(max_age)
ages.append(max_age)
ages.append(min_age)
ages.sort()
print(ages)
print((int(ages[5]+ages[6])/2))
print(sum(ages)/len(ages))


#print((sum/len(ages)))