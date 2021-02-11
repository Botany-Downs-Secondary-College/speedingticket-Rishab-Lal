global SPEED_LIMIT
SPEED_LIMIT = 100
def numberdata_filter(the_input):
    while the_input == str(the_input):
        try:
            the_input = int(the_input)
            if the_input == int(the_input):
                return the_input
        except ValueError:
            try:
                the_input = float(the_input)
                if the_input == float(the_input):
                    return the_input
            except ValueError:
                the_input = input("please enter an arabic numarical")
                continue
            
        else:
            the_input = input("please enter an arabic numarical")
            continue

def speed_check(speed_of_vehical):
    def fine_print():
        if speed_of_vehical == int(speed_of_vehical):
            print("you are {}km/h over the speed limit. You will be fined ${:.2f}.".format(over_limit,fine))
        elif speed_of_vehical == float(speed_of_vehical):
            print("you are {:.2f}km/h over the speed limit. You will be fined ${:.2f}.".format(over_limit,fine))
        #could simplify a lot of the code, but leaving it like this saves me having 2 write many comments. E.g. the elif above could be an else.
    if speed_of_vehical == 0:
        print("the vehical is sationary")
    elif speed_of_vehical < 0:
        print("not possible, please enter correct value")
    elif speed_of_vehical <= 100 and speed_of_vehical >= 1:
        print("vehical is within the range of the speed limit")
    elif speed_of_vehical > 100:
        global over_limit
        over_limit = speed_of_vehical - 100
        global fine
        fine = over_limit * 10
        fine_print()

    

global speed_of_vehical
speed_of_vehical = numberdata_filter(input("how fast was the vehical driving? (Enter value as km/h E.g. '20' or '100'): "))
speed_check(speed_of_vehical)

