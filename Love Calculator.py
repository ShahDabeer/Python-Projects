# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
CONCAT=name1+name2
T=CONCAT.count("t")
R=CONCAT.count("r")
U=CONCAT.count("u")
E=CONCAT.count("e")
TRUE=(T+R+U+E)


L=CONCAT.count("l")
O=CONCAT.count("o")
V=CONCAT.count("v")
E=CONCAT.count("e")
TRUE_1=(L+O+V+E)

TRUE_2=str(TRUE)+str(TRUE_1)
TRUE_2=int(TRUE_2)

if TRUE_2 < 10 or TRUE_2 > 90:
    print(f"Your score is {TRUE_2}, you go together like coke and mentos.")
elif TRUE_2 > 40 and TRUE_2 < 50:
    print(f"Your score is {TRUE_2}, you are alright together.")
else:
    print(f"Your score is {TRUE_2}.")





