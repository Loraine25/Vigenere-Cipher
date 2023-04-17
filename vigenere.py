#Anonuevo, Loraine N.
#BSCPE 1-4
#Problem 3

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mAyooo! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Ask the user's name 
user_name = input(f"\n\033[;45;1;3mWhat is your name? \033[0m")
print(f"\n\033[;1;3mNice to meet you, \033[;100;1;3m" + user_name +"\033[;1;3m!\033[0m")
print("\033[0m\033[;35;1;3mKindly input the text that you want to encrypt!\033[0m")

#Create a python program using Vigenère Cipher to encrypt the message
def vigenere_encryption(message, keyword):
    if message.isalpha():
        #Turns the message and the keyword into uppercase format
        message_uppercase=message.upper()
        keyword_uppercase=keyword.upper()

        #Removes spaces in the message and the keyword
        message_stripped = message_uppercase.replace(" ","")
        keyword_stripped = keyword_uppercase.replace(" ", "")

        #Generating the keyword with the same number of letters with the message
        keyword_match=keyword_stripped*(len(message_stripped)//len(keyword_stripped)+1)
        keyword_match=keyword_match[:len(message_stripped)]

        #Encryption of the message
        encrypted_message=""
        for i in range(len(message_stripped)):
            #Checks if the message is an alphabet
            if message_stripped[i].isalpha():
                #Converts the alphabets of the message into numeric equivalent
                message_numbered=ord(message_stripped[i])-65
                #Converts the key into numeric equivalents
                keyword_numbered=ord(keyword_match[i])-65

                #Encrypts the message with respect to the modulo 26
                encrypted_numbers=(message_numbered+keyword_numbered) %26

                #Matches the new numbers to their new equivalent alphabet
                encrypted_letters=chr(encrypted_numbers+65)

                #Stores the encrypted letters into the variable outside the for loop
                encrypted_message+=encrypted_letters
        return encrypted_message
    else:
        print("Cannot encrypt characters outside of the alphabet.")

#ASKING THE USER FOR THE MESSAGE TO BE ENCRYPTED AND THE KEYWORD
message=input("Input Message here:")
keyword=input("Input Keyword Here:")
encrypted_message=vigenere_encryption(message,keyword)

#Prevents the program from outputting "None" after the "Cannot encrypt characters outside of the alphabet." statement
if encrypted_message==None:
    sys.exit()

