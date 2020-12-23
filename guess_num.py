import random
import colorama
from colorama import init, Fore, Back, Style

class GuessNum:
    def __init__(self):
        colorama.init(autoreset=True)
        print('Welcome to random num guessing')
        self.mode = int(input(f'{Fore.GREEN}Would you like to play computer versus human (1) or human vs computer (2): '))

    def start(self):
        if self.mode == 1:
            num = int(input('Enter a number for the computer to guess: '))
            self.comp_guess(num)
        elif self.mode == 2:
            self.guess_num(10)
        else:
            print(f'{Fore.RED}Please choose choose one of the previous options')

    def guess_num(self,x):
        random_num = random.randint(1, x)
        guess = 0

        while guess != random_num:
            guess = int(input(f'guess a number between 1 and {x}: '))
            if guess > random_num: print('Try a lower number')
            elif guess < random_num: print('Try a higher num')

        print(f'{Fore.GREEN}congrats you got it the number was {Fore.BLUE}{random_num}')
        
    def comp_guess(self, x):
        min_num = 1
        max_num = x
        user_msg = ''

        while user_msg != 'c':
            if min_num != max_num:
                guess = random.randint(min_num, max_num)
            else: 
                guess = max_num

            user_msg = input(f'{Fore.BLUE}Is {Fore.GREEN}{guess}{Fore.BLUE} too high {Fore.GREEN}(H){Fore.BLUE}, too low {Fore.GREEN}(L){Fore.BLUE} or correct{Fore.GREEN}(C){Fore.BLUE}: ').lower()

            if user_msg == 'h':
                max_num = guess - 1
            elif user_msg == 'l':
                min_num = guess + 1
        print(f'{Fore.GREEN}The computer got it, it was {Fore.BLUE}{guess}')

game = GuessNum()
game.start()