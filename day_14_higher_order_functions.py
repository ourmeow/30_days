from functools import reduce
from countries import countries
countriess = ['estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#ex1 
def ex1():
    def upper(words):
        return words.upper()
    upper_words = map(upper,countriess)
    return list(upper_words)
print("EXERCISE 1: ",ex1())

#ex2
def ex2():
    def squared(num):
        return num**2
    squared_nums = map(squared,numbers)
    return list(squared_nums)
print("EXERCISE 2: ",ex2())

#ex3
def ex3():
    def upper(word):
        return word.upper()
    upper_words = map(upper, names)
    return list(upper_words)
print("EXERCISE 3: ",ex3())

#ex4
def ex4():
    def land_filter(word):
        if 'land' in word:
            return True
        return False
    filtered = filter(land_filter, countriess)
    return list(filtered)
print("EXERCISE 4: ",ex4())

#ex5
def ex5():
    def six_char(word):
        if len(word) == 6:
            return True
        return False
    filtered = filter(six_char,countriess)
    return list(filtered)
print("EXERCISE 5: ",ex5())

#ex6
def ex6():
    def filtr(word):
        if len(word) >= 6:
            return True
        return False
    filtered = filter(filtr, countriess)
    return list(filtered)
print("EXERCISE 6: ",ex6())

#ex7
def ex7():
    def e_word(word):
        if word[0] == 'e' or word[0] == 'E':
            return True
        return False
    filtered = filter(e_word,countriess)
    return list(filtered)
print("EXERCISE 7: ",ex7())

#ex8
def ex8():
    def capital(word):
        return word.capitalize()
    
    def filtr(word):
        if word[0] == 'E':
            return True
        return False
    filtered = filter(filtr, map(capital, countriess))
    return list(filtered)
print("EXERCISE 8: ",ex8())

#ex9

def ex9():
    def get_string_list(word):
        if type(word) == str:
            return True
        return False
    filtered = filter(get_string_list, numbers)
    return list(filtered)
print("EXERCISE 9: ",ex9())

#ex10
def ex10():
     def add_nums(num1, num2):
         return int(num1) + int(num2)
     sums = reduce(add_nums, numbers)
     return sums
print("EXERCISE 10: ",ex10())

#ex11
def ex11():
    def conc_string(word1, word2):
        return word1 + ', ' + word2
    conc = reduce(conc_string, countriess)
    return conc
print("EXERCISE 11: ",ex11())

#ex12
def ex12():
    def cat_countries(word):
        if 'land' in word or 'ia' in word or 'island' in word or 'stan' in word:
            return True
        return False
    filtered = filter(cat_countries, countries)
    return list(filtered)
print("EXERCISE 12: ",ex12())

#ex13
def ex13():
    def get_first_letter(word):
        return word[0]
    letters = list(map(get_first_letter,countries))
    def count_letters(acc,letter):
        acc[letter] = acc.get(letter,0) + 1
        return acc
    mapping = reduce(count_letters,letters,{})
    sort = dict(sorted(mapping.items(), key=lambda item: item[1], reverse= True))
    return sort
print("EXERCISE 13: ",ex13())
        
#ex14
def ex14():
    return list(map(lambda x:x[1],filter(lambda x:x[0] < 10,enumerate(countries))))
print("EXERCISE 14: ",ex14())

#ex15
def ex15():
    return list(map(lambda x: x[1], filter(lambda x:x[0] >= len(countries) - 10, enumerate(countries))))
print("EXERCISE 15: ",ex15())

#ex16
def sort_name_cap_pop():
    return sorted(countries, key= lambda x: x['population'], reverse= True)

print("Exercise 15: \n", sort_name_cap_pop())
 #ex17
def sort_loc():
    languages = list(map(lambda x: x['languages'],countries))
    all_lang = reduce(lambda acc, x: acc+ x, languages)
    def counts(acc,lang):
        acc[lang] = acc.get(lang,0) + 1
        return acc
    lang_count = reduce(counts,all_lang,{})
    sort_lang = sorted(lang_count, key= lambda x: x[1], reverse= True)[:10]
    return sort_lang

print("Exercise 16: \n", sort_loc())
     