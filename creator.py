import random

print("Welcome to the character generator!")
print()
print("Let's name the brave adventurers:")

# user inputs 5 names
name1 = input("Character 1: ")
name2 = input("Character 2: ")
name3 = input("Character 3: ")
name4 = input("Character 4: ")
name5 = input("Character 5: ")

#once names are added this will be confirmed with this message 
print("Your Characters are complete!")

#random character role assignment
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior"

elif role_number == 2:
    char_role = "Wizard"

elif role_number == 3:
    char_role = "Potato"


#Character stats between 5 and 10

print('"' + name1 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

#now to multiply the stats by 3 depending on the role

if char_role == "Warrior":
    strength *= 3
elif char_role == "Wizard":
    magic *= 3
elif char_role == "Potato":
    health *= 3

# randomly select the format for stats to print

format_choice = random.random()
if format_choice < 0.1:
    #print stats in binary
    print("strength", bin(strength))
    print("magic", bin(magic))
    print("health", bin(health))
elif format_choice < 0.2:
    #print stats in hex
    print("strength", hex(strength))
    print("magic", hex(magic))
    print("health", hex(health))
else:
    #print stats decimal
    print("strength", strength)
    print("magic", magic)
    print("health", health)

    print()
    print("------")
    print()
#Character 2 role

print()
print("------")
print()

role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior"

elif role_number == 2:
    char_role = "Wizard"

elif role_number == 3:
    char_role = "Potato"

print('"' + name2 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

if char_role == "Warrior":
    strength *= 3
elif char_role == "Wizard":
    magic *= 3
elif char_role == "Potato":
    health *= 3

format_choice = random.random()
if format_choice < 0.1:
    #print stats in binary
    print("strength", bin(strength))
    print("magic", bin(magic))
    print("health", bin(health))
elif format_choice < 0.2:
    #print stats in hex
    print("strength", hex(strength))
    print("magic", hex(magic))
    print("health", hex(health))
else:
    #print stats decimal
    print("strength", strength)
    print("magic", magic)
    print("health", health)

#charcter3
print()
print("------")
print()

role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior"

elif role_number == 2:
    char_role = "Wizard"

elif role_number == 3:
    char_role = "Potato"

print('"' + name3 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

if char_role == "Warrior":
    strength *= 3
elif char_role == "Wizard":
    magic *= 3
elif char_role == "Potato":
    health *= 3

format_choice = random.random()
if format_choice < 0.1:
    #print stats in binary
    print("strength", bin(strength))
    print("magic", bin(magic))
    print("health", bin(health))
elif format_choice < 0.2:
    #print stats in hex
    print("strength", hex(strength))
    print("magic", hex(magic))
    print("health", hex(health))
else:
    #print stats decimal
    print("strength", strength)
    print("magic", magic)
    print("health", health)

#character 4

print()
print("-------")
print()

role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior"

elif role_number == 2:
    char_role = "Wizard"

elif role_number == 3:
    char_role = "Potato"

print('"' + name4 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

if char_role == "Warrior":
    strength *= 3
elif char_role == "Wizard":
    magic *= 3
elif char_role == "Potato":
    health *= 3

format_choice = random.random()
if format_choice < 0.1:
    #print stats in binary
    print("strength", bin(strength))
    print("magic", bin(magic))
    print("health", bin(health))
elif format_choice < 0.2:
    #print stats in hex
    print("strength", hex(strength))
    print("magic", hex(magic))
    print("health", hex(health))
else:
    #print stats decimal
    print("strength", strength)
    print("magic", magic)
    print("health", health)


print()
print("-----")
print()

#charcter 5
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior"

elif role_number == 2:
    char_role = "Wizard"

elif role_number == 3:
    char_role = "Potato"

print('"' + name5 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

if char_role == "Warrior":
    strength *= 3
elif char_role == "Wizard":
    magic *= 3
elif char_role == "Potato":
    health *= 3

format_choice = random.random()
if format_choice < 0.1:
    #print stats in binary
    print("strength", bin(strength))
    print("magic", bin(magic))
    print("health", bin(health))
elif format_choice < 0.2:
    #print stats in hex
    print("strength", hex(strength))
    print("magic", hex(magic))
    print("health", hex(health))
else:
    #print stats decimal
    print("strength", strength)
    print("magic", magic)
    print("health", health)

print()
print("------")
print()


print("Happy adventuring!")