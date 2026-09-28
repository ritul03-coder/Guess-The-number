import random
 
def guess_the_number_game():
    random_value = random.randint(1, 100)
    count = 0
     
    print("Hello! This is the develpoper of the game, thanks for playing!!!")
    print("hello welcome to the game 'guess the numbers'!!")
    print("guess number between 1 to 100")

    """
    This is my project on topic Guess_The_Number_Game in which i have combined several foundational programming concepts to create an interactive command-line application
    Among of all the concepts that i have applied few are Control Flow & Loops,User Input & Data Type Conversion and Libraries & State Management
    """
    
    while True:
        num = input("enter guess: ")
        
        # Checking if it is a integer number or not
        try:
           guess = int(num)
           # This_function_will_check_whether_the_number_passed_is_a_integer_or_not
        except:
           print("invalid input, enter a integer number ")
           continue
           
        count = count + 1
       # This_funtion_will_count_the_number_of_times_the_number_has_been_guessed
       
        if guess < random_value:
            print("too low, make a little bit higher assumption")
        elif guess > random_value:
            print("too high, make a little bit lower assumption")
        else:
            print("Yay you got it!! took you", count, "tries")

     # if-else statement evaluating the score based on the count
            if count <= 4:
                print("awesome, you are a pro player")
            else:
                print(" Oops, better luck next time , you were close to be a pro")
            break

guess_the_number_game()
