import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} is Too High(H) or Too Low(L) or Correct(C) :').lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
    print(f"Oops! Compter guessed your number {guess}")
    
computer_guess(10000)