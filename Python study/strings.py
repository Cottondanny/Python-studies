print("\"Danny's Academy\"") #need to use \ if i want to add ""
phrase="Danny's Academy"
print(phrase + " is awesome") 
print(phrase.lower().islower())
print(phrase.upper())
print(len(phrase))
print(len("I love Danny"))
print(len(phrase + " is awesome"))
print("Danny is cool".lower())
print("Danny is cool".upper().isupper())
print(phrase[0]) #D is at 0 place 
print(phrase.index("D")) #perimeter or the place where the word is at 0,1,2,3
print(phrase.index("Acad")) #can also use words 
print(phrase.replace("Danny","Robin"))
print(phrase.replace("Academy","Home").upper())
print(phrase.replace("Academy","Home").lower() + " is very messy".upper())