users_sentence=input("Enter sentence: ")
users_sentence=users_sentence.lower()  #SO ITS NOT CASE SENSITIVE
users_sentence=users_sentence.replace(" ","")
reverse_sentence=users_sentence[::-1]
if users_sentence==reverse_sentence:
    print("It`s palindrome.")
else:
    print("It is not palindrome.")