import random
import string

def generate_password(lenght):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character) for _ in range(lenght))
    return password 
password_lenght = int(input())
generated_password = generate_password(password_lenght)
print(generated_password)