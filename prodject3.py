
red = 1
orange = 2
yellow = 2
green = 2
purple = 1
ultra_rare_cool_rainbow = 1
print("Today we find out what color skittle you are based on this quiz. enter to play!")
input()

a1 = input("Whats your fave candy flavor, A grape, B green apple, C lemon, D orange, E berry red, F mystery:")
if a1 == "A" or a1 == "a":
    purple += 1
elif a1 == "B" or a1 == "b":
    green += 1
elif a1 == "C" or a1 == "c":
    yellow += 1
elif a1 == "D" or a1 == "d":
    orange += 1
elif a1 == "E" or a1 == "e":
    red += 1
elif a1 == "F" or a1 == "f":
    ultra_rare_cool_rainbow += 1

a2 = input("Whats your fave music genre, A country, B rock, C Kpop, D jazz, E rap, F pop:")
if a2 == "A" or a2 == "a":
    purple += 1
elif a2 == "B" or a2 == "b":
    yellow += 1
elif a2 == "C" or a2 == "c":
    orange += 1
elif a2 == "D" or a2 == "d":
    red += 1
elif a2 == "E" or a2 == "e":
    green += 1
elif a2 == "F" or a2 == "f":
    ultra_rare_cool_rainbow += 1

a3 = input("Whats your fave my little pony chareter , A twilight sparkle , B apple jack, C flutter shy, D pinky pie, E rarity, F rainbow dash:")
if a3 == "A" or a3 == "a":
    purple += 1
elif a3 == "B" or a3 == "b":
    yellow += 1
elif a3 == "C" or a3 == "c":
    orange += 1
elif a3 == "D" or a3 == "d":
    red += 1
elif a3 == "E" or a3 == "e":
    green += 1
elif a3 == "F" or a3 == "f":
    ultra_rare_cool_rainbow += 1

a4 = input("whats your fav food? , A pasta , B pie, C sushi, D ice cream, E pizza, F fruits, :")
if a4 == "A" or a4 == "a":
    purple += 1
elif a4 == "B" or a4 == "b":
    yellow += 1
elif a4 == "C" or a4 == "c" :
    orange += 1
elif a4 == "D" or a4 == "d":
    red += 1
elif a4 == "E" or a4 == "e":
    green += 1
elif a4 == "F" or a4 == "f":
    ultra_rare_cool_rainbow += 1

a5 = input("whats your fav animal? , A jellyfish , B horse, C tiger, D panda , E turtle, F unicorn, G other :")
if a5 == "A" or a5 ==  "a":
    purple += 1
elif a5 == "B" or a5 == "b" or a5 == "G" or a5 == "g" :
    yellow += 1
elif a5 == "C" or a5 == "c" :
    orange += 1
elif a5 == "D" or a5 == "d":
    red += 1
elif a5 == "E" or a5 == "e":
    green += 1
elif a5 == "F" or a5 == "f":
    ultra_rare_cool_rainbow += 1

print("Press Enter to see your results of what color skittle you are!")
input()

# red skittle ending, like when this has most points
if red >= orange and red >= yellow and red >= green and red >= purple and red >= ultra_rare_cool_rainbow:
    print("Your a red skittle!" " Your spontaneous nature and need for adventure makes you a passionate and ambitious individual, "
    "and you also might harbor a slight competitive streak. Are you looking for an opportunity to stand out?" \
    " Do you enjoy being the center of attention? Red is the color choice to let the world know you choose to live life to the fullest.")
# orange skittle ending, like when this has most points
elif orange >= red and orange >= yellow and orange >= green and orange >= purple and orange >= ultra_rare_cool_rainbow:
    print("Your a orange skittle! your said to represent a need for personal physical or social challenges within your life")
    print("a need for healthy respect and acceptance within a group setting.")
# yellow skittle ending, like when this has most points
elif yellow >= orange and yellow >= red and yellow >= green and yellow >= purple and yellow >= ultra_rare_cool_rainbow:
    print("Your a yellow skittle!")
    print(" Yellow as a favorite color is said to represent happiness and a love of learning. You probably love to express your individuality by creating new ideas and sharing your collected knowledge with others")
    print("and might have a deep need for logical order in your everyday life. Yellow is the color of sunshine, and will instantly invite feelings of warmth, happiness, and love into your home.!")
# green skittle ending, like when this has most points
elif green >= orange and green >= yellow and green >= red and green >= purple and green >= ultra_rare_cool_rainbow:
    print("Your a green skittle!")
    print(" it is said that you are typically down to earth and aware of what other people think of you, seeking acknowledgement and acceptance for the everyday things you do.")
    print("A good reputation is very important to you, and you might feel a deep need to feel safe and secure, with a deep longing to love and be loved.")
# purple skittle ending, like when this has most points
elif purple >= orange and purple >= yellow and purple >= green and purple >= red and purple >= ultra_rare_cool_rainbow:
    print("Your a purple skittle!")
    print("said to represent an artistic and unique individual, who is often very intuitive and deeply interested in spirituality. Lovers of purple are said to be a good judge of character,")
    print("and a visionary with a great need to participate in humanitarian issues. Active and compassionate, purple lovers are said to be constantly analyzing and observing everything that crosses their path.")
    print("A little moody sometimes? Maybe, but that's only because you experience and feel everything so deeply.")
# rainbow skittle ending, like when this has most points
elif ultra_rare_cool_rainbow >= orange and ultra_rare_cool_rainbow >= yellow and ultra_rare_cool_rainbow >= green and ultra_rare_cool_rainbow >= purple and ultra_rare_cool_rainbow >= red:
    print("Your a ULTRA RARE RAINBOW skittle!")
    print("you said to represent a loving, kind, and sensitive individual, often with a strong nurturing and sensual side but your also strong and smart and stand up for yourself.")
    print("with a sweet, charming side that often makes you a delicate and lovable individual.and a cool and awsome and amazing side that makes people fear you.")
    print("rainbow often can represent softness a need to be accepted and loved, but in other words your awsome and cool .")
