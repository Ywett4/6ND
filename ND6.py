"""For the first exercise let's continue the mood checking program from before. Ask user to tell you what mood s/he is in:

if the mood is "happy", the program should print out "It is great to see you happy!"
if the mood is "nervous", respond with "Take a deep breath 3 times.". Use elif to enter more if statements: elif mood == "nervous":.
Make up responses also for "sad", "excited" and "relaxed".
The last option should be the normal else, which responds with "I don't recognize this mood"""
# Nuotaikos
nuotaika = input("Apibudinkite savo nuotaika: ")
if nuotaika == "gera":
    print("Puiku matyti tave!")
elif nuotaika == "nervuota":
    print("Ikvek gyliai tris sykius")
elif nuotaika == "liudna":
    print("Neliudek")
elif nuotaika == "uzsidegusi":
    print("Atsivesink!")
elif nuotaika == "atsipalaidavusi":
    print("Pasikisk pagalalve po galva")
else:
    print("Nepazistu taves")

""" We have a first customer - a local Casino! They want to expand their business to computer gambling so they want us to build a gambling game for them. For the beginning something small and simple - a game called Guess the secret number.

Your task is to create this game:

First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.
Then the user has to find out what this number is (using input()). Store user's guess in a variable called guess.
Check if your secret is equal to user's guess.
If the user's guess is wrong, let him/her know that (use print() and if/else).
If the user's guess is correct, congratulate him/her."""

# Atspek skaiciu

paslaptis = 9
x = int(input("Atspek skaiciu: "))
print(f"Jusu spejimas {x}")
if x == paslaptis:
         print("Jusu spejimas laimingas")
else:
         print("Apgailestaujame, Jus neatspejote. Bandykite veliau.")


#Skaiciuotumas

x = int(input("Iveskite pirmaji sk.: "))
veiksmas = input("Iveskite aritmetini veiksma: ")
y = int(input("Iveskite antraji sk.: "))
if veiksmas == "+":
    print(f"ats.: {x + y}")
elif veiksmas == "-":
    print(f"ats.: {x - y}")
elif veiksmas =="*":
    print(f"ats.: {x * y}")
elif veiksmas == "/":
    print(f"ats.: {x / y}")
else:
    print("Parinktas blogas aritmetinis veiksmas")
