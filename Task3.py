#password generator
import random
#function to generate password
def gen_password(length):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits="0123456789"
    symbols="@#₹_&-+/*:;!?%$."
    characters=lower+upper+digits+symbols
    password=" "
    for i in range (length):
        password+=random.choice(characters)
    return password
       
#main part
print("========== password generator ==========")
print("Welcome to password generator")
length=int(input("Enter length of your password:"))
if length<=0:
        print("Password length must be more than 0.Please try again")
elif (length>0):
        your_pass=gen_password(length)
        print("Your password is:", your_pass)   
else:
     print("please enter valid number")