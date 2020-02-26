import math

## Find PI to the Nth Digit ##

def find_pi():
    while True:
        try: 
            num = int(input('How many decimals would you like?: '))
        except ValueError:
            print('Integers only!')
        else:
            if num > 25 or num < 0:
                print('You cannot have an integer larger than 25!!!')
            else:   
                print(round(math.pi, num))
                break
find_pi()

##


