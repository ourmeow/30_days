import datetime
print(dir(datetime))

#ex1
def ex1():
    now = datetime.datetime.now()
    return f'DAY: {now.day}, MONTH: {now.month}, YEAR: {now.year}, HOUR: {now.hour}, MINUTE: {now.minute}, TIMESTAMP: {now.timestamp},'
print('EXERCISE 1: ', ex1())

#ex2
def ex2():
    now = datetime.datetime.now()
    time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
    return time_one
print('EXERCISE 2: ', ex2())

#ex3
def ex3():
    now = datetime.datetime.now()
    date_string = "5 December, 2019"
    date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
    return date_object
print('EXERCISE 4: ', ex3())

#ex4
def ex4():
    now = datetime.date(year=2026,month=3,day=31)
    new_year = datetime.date(year=2027,month=1,day=1)
    diff = new_year - now
    return diff
print('EXERCISE 4: ', ex4())

#ex5
def ex5():
    now = datetime.date(year=2026,month=3,day=31)
    year_past = datetime.date(year=1970,month=1,day=1)
    diff = now-year_past
    return diff
print('EXERCISE 5: ', ex5())