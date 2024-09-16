import random   
import string


length = int(input("Specify the length of password: "))
def password_generator(length):
    lower_character = string.ascii_lowercase
    upper_character = string.ascii_uppercase
    digit = string.digits
    other_character = string.punctuation

    combine_characters = lower_character + upper_character +digit + other_character

    password = [random.choice(lower_character),random.choice(upper_character)
                ,random.choice(digit),random.choice(other_character)]
    
    password += random.choices(combine_characters,k=length-4)

    random.shuffle(password)

    return ''.join(password)

final_password = password_generator(length)
print(f"Generated password: {final_password}")




 
