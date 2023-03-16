print("==Which Pokemon are you?==")
print()
print("(All answers","\033[31m","MUST","\033[0m","be in lowercase)")
print()
Pikachu = input("Do you like shocking everyone around you?")
if Pikachu == ("yes"):
  print("It seems like you must be Pikachu!")
print()
Squirtle = input("Do you like hanging out with your squad?")
if Squirtle == ("yes"):
  print("Cool, you're Squirtle!")
print()
Bulbasaur = input("Do you try to look out for all your friends?")
if Bulbasaur == ("yes"):
  print("Nice, you're Bulbasaur!")
print()
Charmander = input("Are you loyal to your friends?")
if Charmander == ("yes"):
  print("Neat, you're Charmander!")
else:
  print()
  print("""Well...
  I guess you're not a Pokemon then!""")