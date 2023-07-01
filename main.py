import random
list_of_all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '=', '{', '[', '}' ,'}', '?', '0',  '1', '2', '3', '4', '5', '6', '7', '8', '9']

palash = "-"
temp_password = ' '

for i in range(12):
    temp_password = temp_password + random.choice(list_of_all)

password1 = temp_password[:5] + palash + temp_password[5:]
password = password1[:10] + palash + password1[10:]

print(f"Hey Palash your password is: {password}")

