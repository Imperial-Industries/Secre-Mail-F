import time
print("Secre-Mail F is loading...")
time.sleep(1)
newMessage = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print("Please wait...")
time.sleep(1)
warning = input("The messages encrypted and decrypted should ONLY be used along with the Secre-Mail client. Are you sure you want to continue (y/n) - ")
if warning == "y":
    print("The Secre-Mail client can be accessed at secre-mail.bubbleapps.io. Take a minute to copy that link.")
    time.sleep(3)
    pass
if warning == "n":
    print("Program terminated")
    exit()
option = input("Do you want to encrypt a message (y/n) - ")
optionVerif = input("Are you sure (y/n) - ")
if optionVerif == "y":
    pass
if optionVerif == "n":
    while optionVerif == "n":
        option = input("Do you want to encrypt a message (y/n) - ")
        optionVerif = input("Are you sure (y/n) - ")
if option == "y":
    key = int(input("Please enter the displacement value of the letters (number, negative or positive) - "))
    keyVerif = input("Are you sure (y/n) - ")
    if keyVerif == "y":
        pass
    if keyVerif == "n":
        while keyVerif == "n":
            key = int(input("Please enter the displacement value of the letters (number) - "))
            keyVerif = input("Are you sure (y/n) - ")
    message = input("Please enter the message you want to encrypt (message) - ")
    messageVerif = input("Are you sure (y/n) - ")
    if messageVerif == "y":
        pass
    if messageVerif == "n":
        while messageVerif == "n":
            message = input("Please enter the message you want to encrypt (message) - ")
            messageVerif = input("Are you sure (y/n) - ")
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key)%26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print("Encrypted message - " + newMessage)
    finalMessage = input("Would you like to add the displacement value at the end (y/n) - ")
    finalVerif = input("Are you sure (y/n) - ")
    if finalVerif == "y":
        pass
    if finalVerif == "n":
        while finalVerif == "n":
            finalMessage = input("Would you like to add the displacement value at the end (y/n) - ")
            finalVerif = input("Are you sure (y/n) - ")
    if finalMessage == "y":
        print("New encrypted message - " + newMessage + " k" + str(key))
        print("Program terminated")
        exit()
    if finalMessage == "n":
        print("Encrypted Message - " + newMessage)
        print("Program terminated")
        exit()
else:
    pass
option = input("Do you want to decrypt a message (y/n) - ")
optionVerif = input("Are you sure (y/n) - ")
if optionVerif == "y":
    pass
if optionVerif == "n":
    while optionVerif == "n":
        option = input("Do you want to decrypt a message (y/n) - ")
        optionVerif = input("Are you sure (y/n) - ")
if option == "y":
    optionVerifYkey = input("To decrypt a value, you WILL need the displacement value/key. Are you sure you want to continue (y/n) - ")
    if optionVerifYkey == "y":
        pass
    if optionVerifYkey == "n":
        print("Program terminated")
        exit()
    key = int(input("Please enter the key value (number, negative or positive) - "))
    keyVerif = input("Are you sure (y/n) - ")
    if keyVerif == "y":
        pass
    if keyVerif == "n":
        while keyVerif == "n":
            key = int(input("Please enter the key value (number, negative or positive) - "))
            keyVerif = input("Are you sure (y/n) - ")
    message = input("Please enter the encrypted message (message) - ")
    messageVerif = input("Are you sure (y/n) - ")
    if messageVerif == "y":
        pass
    if messageVerif == "n":
        while messageVerif == "n":
            message = input("Please enter the encrypted message (message) - ")
            messageVerif = input("Are you sure (y/n) - ")
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key)%26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print("Decrypted message - " + newMessage)
    print("Program terminated")
    exit()
else:
    print("Program terminated")
    exit()
