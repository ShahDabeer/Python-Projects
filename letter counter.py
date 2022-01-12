print("Welcome To the letter counter app")

user_message=input("Enter your Message")
user_letter=input("Enter the letter")


print(user_message)
print(user_letter)

count_msg=user_message.count(user_letter)


len_msg=len(user_message)
perc=count_msg/len_msg*100

print("The count of the letter",user_letter, " is ",count_msg)
print("The percentage of letter",user_letter, " is ",perc)

