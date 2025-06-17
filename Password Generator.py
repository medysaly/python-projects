import random
import string

user_num = int(input('Please enter a number: '))

letter = string.ascii_letters
single_letters = list(letter)
num_user = string.digits
single_num = list(num_user)
punc_user = string.punctuation
single_punc = list(punc_user)

list_user = single_letters + single_num + single_punc

password = random.sample(list_user,user_num)
print("".join(password))
