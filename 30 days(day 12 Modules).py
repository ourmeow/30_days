#ex1
import string, random 
def random_user_id():
    characters = string.ascii_letters + string.digits
    username = ''
    for i in range(6):
        username += random.choice(characters)
    return username


def user_id_gen_by_user():
    num_of_characters = int(input("enter number of characters: "))
    num_of_generators = int(input("Enter how many ids would you like to create: "))
    characters = string.ascii_letters + string.digits
    name = ''
    usernames = []
    for i in range(num_of_generators):
        for c in range(num_of_characters):
            name += random.choice(characters)
            
        usernames.append(name)
        name = ''
    return usernames

def rgb_color_gen():
    list_of_colours = []
    for color in range(3):
        list_of_colours.append(random.randrange(0,255))
    return f"rgb({list_of_colours[0]},{list_of_colours[1]},{list_of_colours[2]})"


def list_of_hexcolors(type,number):
    characters = '0123456789abcdef'
    hexcolor = '#'
    rgb_string = ''
    hex_list = []
    rgb_list = []
    if type == 'hexa':
        for i in range(number):
            for j in range(6):
                hexcolor += random.choice(characters)
            hex_list.append(hexcolor)
            hexcolor = '#'
        return hex_list
    elif type == 'rgb':
        for color in range(number):
            rgb_list.append(f"rgba({random.randrange(0,255)},{random.randrange(0,255)},{random.randrange(0,255)})")
        return rgb_list
    
def shuffle_list(list:list):
    if len(list) > 1:
        new_list = random.shuffle(list)
        return new_list
    else:
        return "list does not contain anything!"





