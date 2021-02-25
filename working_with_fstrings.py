first_name = "ada"
last_name = "lovelace"
#This is an f-string. For Python 3.6 and up
full_name = f"{first_name} {last_name}"
message_1 = f"Hello, {full_name.title()}!"
print(message_1)

#This is how you do it for Python 3.5 and before
message_2 = "Hello, {} {}!".format(first_name,last_name).title()
print(message_2)

#or
message_3 = "Hello, {}!".format(full_name).title()
print(message_3)
