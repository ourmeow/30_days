empty = ()
brothers= ('Viktor','Keeper','Loonie')
sisters = ('Viktoria','Teresa','Kate')
counting_brothers = len(brothers)
print(counting_brothers)
siblings = brothers + sisters
print(siblings)
count_siblings = len(siblings)
print(count_siblings)
parents = ('Lena',"Alex")
family_members = siblings + parents
print(family_members)

first,second,three,four,five,six,seven,eight = family_members

new_parents = family_members[6:8]
print(new_parents)
new_siblings = family_members[:6]
print(new_siblings)
fruits = ('mandarin','apple', 'orange')
vegetables = ('cucumbers', 'tomato', 'celery')
animal_products = ('pork','beef','milk')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_ls = list(food_stuff_tp)
middle = food_stuff_tp[4:5]
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[6:9]

del food_stuff_tp

