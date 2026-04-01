

#ex1
def ex1():
    names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
    try:
        *nordic_countries, es, ru = names
        return nordic_countries , es, ru
    except Exception as e:
        print(e)
    
nordic, es, ru = ex1()
print("Exercise 1: ", f"NORDIC: {nordic}, ES: {es}, RU: {ru}")
