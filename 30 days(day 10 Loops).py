

#ex1
def ex1():
    for i in range(11):
        print(i)

def ex2():
    for i in range(10,-1,-1):
        print(i)
def ex3():
    for i in range(8):
        print('#' * i)

def ex4():
    for i in range(9):
        for j in range(9):
            print('# ', end=' ')
        print()


def ex5():
    for i in range(11):
        result = i * i
        print(f"{i} x {i} = {result}")

def ex6():
    pg_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
    for i in pg_list:
        print(i)

def ex7():
    for i in range(101):
        if i % 2 == 0 and i != 0:
            print(i)
        
def ex8():
    for i in range(101):
        if i % 2 != 0:
            print(i)

def ex9():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)

def ex10():
    sum_even = 0
    sum_odd = 0
    for i in range(101):
        if i % 2 == 0:
            sum_even += i
        if i % 2 != 0:
            sum_odd += i
    print(f"Even: {sum_even} Odd: {sum_odd}")

def ex12():
    countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
    for i in countries:
        if 'land' in i :
            print(i)

def ex13():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    reversed_fruits = []

    for i in fruits:
        reversed_fruits.insert(0,i)
    print(reversed_fruits)

from countries_data import countries
def ex14():
    count = set()
    for country in countries:
        for detail in country["languages"]:
            count.add(detail)
    print(len(count))

def ex15():
    language_count = {}

    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = sorted(language_count.items(),key = lambda item: item[1],reverse = True)
    print("top 10: ")
    for lang,count in sorted_languages[:10]:
        print(lang,count)
def more_lang():
    languages = {}
    for country in countries:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else: 
                languages[language] = 1

    sorted_languages = sorted(languages.items(), key = lambda item: item[1],reverse=True)
    for i in sorted_languages[:10]:
        print(i)
def more_pop():
    sorted_pop = sorted(countries,key= lambda country: country['population'],reverse=True)
    for i in sorted_pop[:10]:
        print(i["name"],i["population"])

more_pop()         

  
        



        


