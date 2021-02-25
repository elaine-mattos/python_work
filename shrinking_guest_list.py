guests=["john lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

print(f"Dear {guests[0].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[1].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[2].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[3].title()}, you are invited to my dinner party.\n")


print("Hey guys! I just found a bigger table!!!")

guests.insert(0,"Mick Jagger")
guests.insert(2,"Keith Richards")
guests.append("Jimmy Hendrix")


print(f"Dear {guests[0].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[1].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[2].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[3].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[4].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[5].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[6].title()}, you are invited to my dinner party.\n")

print("-----------------------------------------------")
print("I'm really sorry but the table won't arrive on time and I can only invite 2 lucky bastards.\n")

print(f"I'm sorry {guests.pop()}, I'm afraid I can't do that.\n")
print(f"I'm sorry {guests.pop()}, I'm afraid I can't do that.\n")
print(f"I'm sorry {guests.pop()}, I'm afraid I can't do that.\n")
print(f"I'm sorry {guests.pop()}, I'm afraid I can't do that.\n")
print(f"I'm sorry {guests.pop()}, I'm afraid I can't do that.\n")

print("-----------------------------------------------")

print(f"Dear {guests[-2].title()}, you are STILL invited to my dinner party.\n")
print(f"Dear {guests[-1].title()}, you are STILL invited to my dinner party.\n")


print("-----------------------------------------------")
print("I have changed my mind. There will be no freaking dinner party.\n")


del guests[0]
del guests[0]
print(guests)
