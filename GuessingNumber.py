import random
import math 
lower = int(input("Enter lower bound:- ")) #Taking user minimum range
upper = int(input("\nEnter upper bound:- ")) #Taking user maximum range
random_number = random.randint(lower,upper) #Generating a random number between given range 
print("\n\tYou'v only ", round(math.log(upper - lower + 1,2)), "chance to get the integer!\n")
count = 0 #initialization number of guesses 
#for calculation of minimum number of 
#guesses depend upon range 
while count < math.log(upper - lower + 1,2):
    count += 1 
    guess = int(input("Guess a number:- ")) #Taking guessing number as input 
    #Condition testing 
    if random_number == guess:
        print("Congratulations you did it in ", count, " try")
        #Once guessed loop will break 
        break 
    elif random_number > guess:
        print("You guessed too small!")
    elif random_number < guess:
        print("You guessed too high!") 
#If guessing is more than required guesses,
#So this output.
if count > math.log(upper - lower + 1,2):
    print("\nThe number is %d" % random_number)
    print("\tBetter Luck Next time!")

