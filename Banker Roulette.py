import random

print("Welcome to Banker Roulette")
print("Whose name comes out has to pay the bills")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items=len(names)
random_item= random.randint(0, num_items-1)
person_pay=names[random_item]
print(person_pay + " has to pay the bill")
