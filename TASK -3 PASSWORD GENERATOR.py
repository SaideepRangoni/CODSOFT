import random
import string
length_of_password=int(input("enter the specified length of the password: "))
special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
password_char=string.ascii_letters + string.digits + special_characters

password=''.join(random.choice(password_char) for i in range(length_of_password))
print("Generated random password is:",password)