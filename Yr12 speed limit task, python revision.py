
import os
def speedinput(x):
    y = str
    while type(y) != int:
        try:
            if x == 2:
                y = int(input("enter your vehical speed: ")) #no.2
            else:
                y = int(input("enter a the speed limit: ")) #no.1
        except:
            print("please enter a a valid numarical")
        else:
            print("value accepted")

    print("returning result")
    return int(y) 

valid_answers = ["Y", "N"]
speeding_question = input("did you speed? (enter Y/N): ")
x = 1

if speeding_question.upper().strip() in valid_answers[0]:
    x = 1
    number_1 = speedinput(x)
    x += 1
elif speeding_question.upper() in valid_answers[1]:
    print("why are you here?")
    number_1 = 0
    number_2 = 0
else:
    x = 1
    run = 1
    if run == 1:
        print("invalid responce, plase try again")
        run += 1

    while speeding_question.upper() not in valid_answers[0]:
        speeding_question = input("did you speed? (enter Y/N): ")
        if speeding_question.upper() in valid_answers[1]:
            print("why are you here?")
            number_1 = 0
            number_2 = 0
            break
        if speeding_question.upper() not in valid_answers:
            print("invalid responce, plase try again")

if x == 1 and speeding_question.upper() in valid_answers[0]:
    number_1 = speedinput(x)
    x += 1
if speeding_question.upper() in valid_answers[0]:
    number_2 = speedinput(x)

if number_1 >= number_2:
    print("you are fined $50 for wasting my time.")
elif number_1 < 0 or number_2 < 0:
    print("you are fined $50 for wasting my time.")
elif number_1 < number_2:
    over_speed = number_2 - number_1
    fine = 0.5*(over_speed**2)
    print("you drove {}kmh^-1 over the speed limit".format(int(over_speed)))
    print("you will accordingly be fined ${}".format(fine))

print("end code")
        
        
        
    









