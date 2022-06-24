def encrypt():
    message=input("enter the message you want to encrypt")
    ascii_message=[ord(char)+3 for char in message]
    encrypt_message=[chr(char)for char in ascii_message]
    print(''.join(encrypt_message))
def decrypt():
    message=input("enter the message you want to decrypt")
    ascii_message=[ord(char)for char in message]
    decrypt_message=[chr(char)for char in ascii_message]
    print(''.join(decrypt_message))
flag=True
while flag==False:
    choice=input("what do you want to do?\n1.encrypt a message 2.descrypt a message \n")
    if choice=="e":
        print("encrypt")
    elif choice=="d":
        print("decrypt")
    else:
        play_again=input("do you want to try again or do you want to exit?(y/n)")
        if play_again=="y":
            continue
        elif play_again=="N":
            break
encrypt()
decrypt()
