import random

# random.randrange (start, stop)
# random.randrange (0, 11)
# 11 will not be included

#r = random.randrange(-5, 11)
# print(r)

# random.randint (start, stop)
# random.randint (0, 11)
# 11 will be included

top_of_range = input("Type a number: ")

# make sure if the input is integer/ number or not. WHat if it is Hello, or something

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time ")
        quit()

else:
    print("Please type a number next time. ")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0


while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number")

        else:
            print("You were below the number")


print("You got it in", guesses, "guesses")