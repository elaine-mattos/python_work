guests=["john lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

print(f"Dear {guests[0].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[1].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[2].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[3].title()}, you are invited to my dinner party.\n")

#print(f"Dear {guests.pop().title()}, I'm sorry to hear you won't make it to the dinner party\n")
print(f"Dear {guests[3].title()}, I'm sorry to hear you won't make it to the dinner party\n")
guests[3] = "Eric Clapton"
#guests.append("Eric Clapton")

print(f"Dear {guests[0].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[1].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[2].title()}, you are invited to my dinner party.\n")
print(f"Dear {guests[3].title()}, you are invited to my dinner party.\n")
