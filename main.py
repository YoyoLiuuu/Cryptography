# This program is by Yoyo Liu 
# Completed May 5 2021
# Uploaded to Github 1/21/2024

import string
def is_valid_shift_number():
 valid_shift_number = False
 while valid_shift_number == False:#run this again and again until a correct shift number is entered
   shift_number = int(input("How many digits do you want your message/encryption to be shifted? (For decryption, enter the number used to encrypt)\n"))#ask user to input shift number
   if 0<shift_number<=25: #see if the number is correct
     valid_shift_number = True
     return shift_number #return shift number
   else:
     valid_shift_number = False
     print("Please enter a number between 1 and 25.\n")
#verify if the shift-number is valid
 
def input_message():
 valid_message = False
 while valid_message == False:#run this again and again until valid message is inputed
   message = input("Please enter the message you want to encrypt: (Capital & lowercase numbers are fine, but please do not enter any numbers, spaces, or punctuation as the system will delete them even if you enter it, thank you!)\n")
   if message.isdigit():
     valid_message = False
     print("Sorry, you entered a message with only numbers, please enter a valid text.")#if the message is only with numbers, ask the user to re-input
   else:
     valid_message = True
 if valid_message == True:
   message = message.translate({ord(c): None for c in string.whitespace})#take out all spaces
   message = message.translate(str.maketrans('', '', string.punctuation))#take out all punctuation
   message = ''.join([i for i in message if not i.isdigit()])#take out all numbers
   return message#if message is valid, return message
 
def shift(n, a_list):#get a shift number and list of numbers to shift
 for i in range(0, len(a_list)):
   a_list[i] = int(a_list[i])#change the string into integer values
   a_list[i] += n#shift the values
 return a_list#return shifted list
 
def encode_message(n,m):
 text_to_num = list(map(lambda p: '{:03}'.format(ord(p)), m))#make text message into decimal values and turn it into list, change all to triple digit for easier calculation
 encoded_num_mess = shift(n, text_to_num)#shift using shift number
 for i in range(0, len(encoded_num_mess)):
   if encoded_num_mess[i] >122 or 90<encoded_num_mess[i]<97:
     encoded_num_mess[i] -=26#if after shifting, the value corresponds to punctuations, change is back to letters by subtracting 26
 return encoded_num_mess#return the encoded number message
 
def num_to_mess(a_list):
 characters = [chr(n) for n in a_list]#change all the strings into int
 end_mess = "".join(characters)#change list into string
 end_mess = end_mess.translate({ord(c): None for c in string.whitespace})#take out spaces, is there are any, just in case
 return end_mess#return the string
 
def input_encryption():
 valid_message = False
 while valid_message == False:#make this run again and again until valid message is inputted
   message = input("Please enter the message you want to decrypt: (Please note: the message should not include any numbers, spaces, or punctuation. If your encryption includes them, they will be taken out. And the message will not be guaranteed to be accurate, thank you!)\n")
   if message.isdigit():
     valid_message = False
     print("Sorry, you entered a message with only numbers, please enter a valid text.")#if the message is composed with only numbers, ask a re-enter
   else:
     valid_message = True
 if valid_message == True:
   message = message.translate({ord(c): None for c in string.whitespace})#take out all spaces
   message = message.translate(str.maketrans('', '', string.punctuation))#take out all punctuation
   message = ''.join([i for i in message if not i.isdigit()])#take out all numbers
   return message#if message is valid, return the message
 
def decode_message(n,m):
 text_to_num = list(map(lambda p: '{:03}'.format(ord(p)), m))##make text message into decimal values and turn it into list, change all to triple digit for easier calculation
 n *= -1#make it shift the other direction
 decoded_num_mess = shift(n, text_to_num)#shift the message
 for i in range(0, len(decoded_num_mess)):
   if decoded_num_mess[i] <65 or 90<decoded_num_mess[i]<97:
     decoded_num_mess[i] +=26#if after shifting, the value corresponds to punctuations, change is back to letters by adding 26
 return decoded_num_mess#return the decoded number message
 
start_up = int(input("Hello, welcome to caesar encryption system, enter 1 to encrypt a message, 2 to decrypt a message.\n"))#ask the user to encrypt or decrypt
 
if start_up == 1:#if user want to encrypt
 start = is_valid_shift_number()#detect shift number
 message = input_message()#detect message
 encode_num = encode_message(start, message)#encode message
 encode_char = num_to_mess(encode_num)#change message from decimal value to string
 print("Here is the encoded message:\n", encode_char, "\nThank you for using the system, bye!")#display encryption
elif start_up == 2:#if user want to decrypt
 encrypt_mess = input_encryption()#ask for encrypted message
 being_shifted = is_valid_shift_number()#detect shift number
 decrypt_num = decode_message(being_shifted, encrypt_mess)#decode message
 decode_char = num_to_mess(decrypt_num)#change message to string
 print("Here is the decoded message: \n", decode_char, "\nThank you for using the system, bye!")#print our decoded message
else:
 print("Sorry, the system did not detect 1 or 2. Bye!")#if user didn't choose 1 or 2, program ends
