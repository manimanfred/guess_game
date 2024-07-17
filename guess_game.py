def guess_game():
    import random
    hidden = random.randrange(1, 20)
    
    while True:
        user_input = input('Please guess a number between 1 to 20: ')
        
        if user_input == 'x':
            print("Sad to see you leaving early")
            exit()

        if user_input == 's':
            print("The hidden value is ", hidden)   
            continue
        
        guess = int(user_input)
        if guess == hidden:
            print("CONGRATULATIONS !!!!!, YOU WON $100,000")
        elif guess > 20:
            print("Kindly guess a number lower than 20")
        elif guess > hidden:
            print("Your number was higher than the chosen number which is :  " + str(hidden))
            print("Try again")
        elif guess < hidden:
            print("Your number was lower than the chosen number which is :  " + str(hidden))
        else:
            print("Your guess is too high than 20")

        while guess != hidden:
            guess_game()

guess_game()