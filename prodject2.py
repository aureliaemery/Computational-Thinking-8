print("What is your name")
name = input("type message:")
print(f"Will you go to the zoo with me {name}")
one = input("type message:")
if one == "yes":
    print(f"Okay {name} get in ma car lets go to the ZOO")
elif one == "no":
    print(f"I dont care were going to the zoo {name}")
else:
    print("Answer only yes or no")
    one = input("type message:")
    if one == "yes":
        print(f"Okay {name} get in ma car lets go to the ZOO")
    elif one == "no":
        print(f"I dont care were going to the zoo {name}")
print(f" Okay {name} were here get out")
print("Do you wanna get food first or see animals first")
two = input("type message:") 
if two == "animals":
    print(f"Okay {name} should we look at the gorilla, tiger, or giraffe?")
    three = input("type message:")
    if three == "gorilla":
        print(f"OMG {name} i love gorillas i was hoping you chose that them! ")
    elif three == "tiger":
        print("Okay whatever yous ay but i think hat tigers are terrifying.")
    elif three == "giraffe":
        print(f"Okay cool! i still dont understand how we have giraffes and no unicorns...")
    else:
        print("choose from gorilla, tiger, or giraffe!")
    print("Okay some of those animals were pretty scary im gonna go home now but thanks fo coming with me to the zoo.")
elif two == "food":
    print(f"Okay {name} cotton candy, fruit juice, or popcorn?")
    two = input("type message:")
    if two == "cotton candy":
            print(f"OMG {name} i also love cotton candy i love the way it melts in my mouth! ")
    elif two == "fruit juice":
            print("mhmmm yummy fruit juice.")
    elif two == "popcorn":
            print("Eww the kernels keep getting stuck in my teeth...")
    else:
            print("choose from cotton candy, fruit juice, or popcorn!")
    print ("Im bored of the zoo the food maid my stomach hurt i need to go you can stay if you want to tough. bye.")
else:
    print("animals or food!")





