from countries_data import countries
from functools import reduce
#ex15
def sort_name_cap_pop():
    return sorted(countries, key= lambda x: x['population'], reverse= True)

print("Exercise 15: \n", sort_name_cap_pop())
 #ex16
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
     