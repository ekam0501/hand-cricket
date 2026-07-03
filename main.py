import random

elements = ["batting", "bowling"]
toss_elements = ["odd", "even"]
valid_numbers = [1, 2, 3, 4, 5, 6]

your_score = 0
computer_score = 0
wickets = 3



def toss():
    your_toss_number = int(input("Enter your toss number (1-6): "))

    while your_toss_number not in valid_numbers:
        your_toss_number = int(input("Enter a number between 1 and 6: "))

    computer_toss_number = random.choice(valid_numbers)

    print(f"Computer toss number = {computer_toss_number}")

    return your_toss_number + computer_toss_number


def computer_is_bowling():
    global your_score
    global wickets

    wickets = 3
    balls = 10

    while wickets != 0:

        your_number = int(input("Enter your number: "))

        while your_number not in valid_numbers:
            your_number = int(input("Enter a number between 1 and 6: "))

        computer_number = random.choice(valid_numbers)

        print(f"Your number = {your_number}")
        print(f"Computer number = {computer_number}")
        balls -= 1


        if your_number == computer_number:

            wickets -= 1
            print(f"OUT! {wickets} wicket(s) and {balls} balls left")

            if wickets == 0:
                print("ALL OUT!")
                print(f"Computer target = {your_score + 1}")
                break

        else:

            your_score += your_number
            print(f"Your score = {your_score} and {balls} balls left")


        if balls == 0:

            break



def computer_bats_first():
    global computer_score
    global wickets

    wickets = 3
    balls = 10

    while wickets != 0:

        your_number = int(input("Enter your number: "))

        while your_number not in valid_numbers:
            your_number = int(input("Enter a number between 1 and 6: "))

        computer_number = random.choice(valid_numbers)

        print(f"Your number = {your_number}")
        print(f"Computer number = {computer_number}")
        balls -= 1

        if your_number == computer_number:

            wickets -= 1
            print(f"OUT! {wickets} wicket(s) left")

        else:

            computer_score += computer_number
            print(f"Computer score = {computer_score} and {balls} balls left")

        if wickets == 0:
            print("ALL OUT!")
            print(f"Your target = {computer_score + 1}")
            break


        if balls == 0:
            break


def user_chases_target():
    global your_score
    global computer_score
    global wickets

    wickets = 3
    balls = 10

    while wickets != 0:

        your_number = int(input("Enter your number: "))

        while your_number not in valid_numbers:
            your_number = int(input("Enter a number between 1 and 6: "))

        computer_number = random.choice(valid_numbers)

        print(f"Your number = {your_number}")
        print(f"Computer number = {computer_number}")
        balls -= 1

        if your_number == computer_number:

            wickets -= 1
            print(f"OUT! {wickets} wicket(s) left")

        else:

            your_score += your_number
            print(f"Your score = {your_score} and {balls} balls left")

            if your_score > computer_score:
                print("YOU CHASED THE TARGET!")
                print("YOU WIN!")
                break

        if wickets == 0:
            print("ALL OUT!")
            print("COMPUTER WINS!")
            break

        if balls == 0:
            break



def computer_chases_target():
    global computer_score
    global your_score
    global wickets

    wickets = 3
    balls = 10

    while wickets != 0:

        your_number = int(input("Enter your number: "))

        while your_number not in valid_numbers:
            your_number = int(input("Enter a number between 1 and 6: "))

        computer_number = random.choice(valid_numbers)

        print(f"Your number = {your_number}")
        print(f"Computer number = {computer_number}")
        balls -= 1

        if your_number == computer_number:

            wickets -= 1
            print(f"OUT! {wickets} wicket(s) left")

        else:

            computer_score += computer_number
            print(f"Computer score = {computer_score} and {balls} balls left")

            if computer_score > your_score:
                print("COMPUTER CHASED THE TARGET!")
                print("COMPUTER WINS!")
                break

        if wickets == 0:
            print("ALL OUT!")
            print("YOU WIN!")
            break

        if balls == 0:
            break



you = input("Odd or even? ").lower()

while you not in toss_elements:
    you = input("Please enter odd or even: ").lower()

toss_total = toss()

if you == "odd":
    user_won_toss = toss_total % 2 == 1
else:
    user_won_toss = toss_total % 2 == 0

if user_won_toss:

    user_choice = input("Batting or bowling? ").lower()

    while user_choice not in elements:
        user_choice = input("Batting or bowling? ").lower()

    if user_choice == "batting":

        print("YOU BAT FIRST")
        computer_is_bowling()

        print("NOW COMPUTER BATS")
        computer_chases_target()

    else:

        print("COMPUTER BATS FIRST")
        computer_bats_first()

        print("NOW YOU BAT")
        user_chases_target()

else:

    computer_choice = random.choice(elements)

    print(f"Computer chose {computer_choice}")

    if computer_choice == "batting":

        print("COMPUTER BATS FIRST")
        computer_bats_first()

        print("NOW YOU BAT")
        user_chases_target()

    else:

        print("YOU BAT FIRST")
        computer_is_bowling()

        print("NOW COMPUTER BATS")
        computer_chases_target()

print("\\nFINAL SCORES")
print(f"Your score = {your_score}")
print(f"Computer score = {computer_score}")


if your_score > computer_score:

    print("YOU WIN!!!")

if your_score == computer_score:

    print("TIE!")

if computer_score > your_score:

    print("COMPUTER WINS!!!")