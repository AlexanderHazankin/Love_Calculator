print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1.lower()+name2.lower()

true = str(name.count("t")+name.count("r")+name.count("u")+name.count("e"))
love = str(name.count("l")+name.count("o")+name.count("v")+name.count("e"))
score = int(true+love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
