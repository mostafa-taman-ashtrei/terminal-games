import random
import string
import colorama
from colorama import init, Fore, Back, Style
from utils.words import words 

class Hangman:
    def __init__(self):
        colorama.init(autoreset=True)
        self.word = random.choice(words)

        while '-' in self.word or ' ' in self.word: self.word = random.choice(words)
        self.word = self.word.upper()
        print('Welcome to hangman!')
        
    def hangman(self):
        word_letters = set(self.word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        lives = 6

        while len(word_letters) > 0 and lives > 0:
            print(f'{Fore.BLUE}You have {Fore.GREEN}{lives} left {Fore.YELLOW}used Letters :', ' '.join(used_letters))
            
            word_list = [letter if letter in used_letters else '_' for letter in self.word]
            print('Current Word:', ' '.join(word_list))

            user_letter = input('Guess a letter: ').upper()
            
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)  

                if user_letter in word_letters: word_letters.remove(user_letter)
                else: 
                    lives = lives - 1
                    print(f'The letter {user_letter} is not in this word')

            elif user_letter in used_letters: print(f'{Fore.RED}You have already used that {user_letter}, try again')
            else: print(f'{Fore.RED}That is not a  valid letter, you can only use one letter at a time')

        if lives == 0: print(f'{Fore.RED}Sorry you are out of lives the word was {Fore.BLUE}{self.word}')
        else: print(f'{Fore.GREEN}Congrats you got it, the word was {Fore.BLUE}{self.word}')    

game = Hangman()
game.hangman()