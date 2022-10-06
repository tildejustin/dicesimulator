import random
# counts how many tries it takes to get snake eyes
count = 0
# counts the interations of the inner loop it takes to get snake eyes first try
count2 = 0
# keeps track of the longest run of the snake eyes loop, for statistic's sake
longest = 1

# loop and a half * 2 = three loops?
# keeps track of inner loop attempts
def main():
    global count, count2, longest
    while True:
        # dice rolling logic
        while True:
            # increment counter for attempts for snake eyes
            count += 1
            # get the random nums for the dice
            firstroll = random.randint(1, 6)
            secondroll = random.randint(1, 6)

            # checks two inputs for equality and outputs "=" or "≠"
            equal = lambda one, two : "=" if one == two else "≠"

            # prints the two numbers and an equal or not equal sign between them
            print(f"Rolled: {firstroll} {equal(firstroll, secondroll)} {secondroll}")

            # if snake eyes, check if it's the longest attempt yet and log if so, then exit the loop
            if firstroll == 1 and secondroll == 1:
                if count > longest:
                    longest = count

                # plural checking, there's got to be a better way to do this
                if count > 1:
                    print (f"It took {count} rolls to get snake eyes.\n")
                else:
                    print (f"It took {count} roll to get snake eyes.\n")
                break
                
        # counter of how many times the upper loop completes
        count2 += 1

        # if inner loop gets snake eyes first try, it's done
        if count == 1:
            break

        # finally, reset inner count after the logic check
        count = 0

    print("Results:")
    print(f"The longest streak was {longest}")
    print(f"It took {count2} tries to get snake eyes in one try")

if __name__ == "__main__":
    main()
