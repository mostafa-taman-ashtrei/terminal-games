import random 
import colorama
from colorama import init, Fore, Back, Style

class RockPaperScissors:
    def __init__(self):
        colorama.init(autoreset=True)
        self.user = input(f'{Fore.BLUE}Choose {Fore.GREEN}(R){Fore.BLUE} for rock {Fore.GREEN}(P){Fore.BLUE} for paper or {Fore.GREEN}(S){Fore.BLUE} for scissors: ').lower()
        self.computer = random.choice(['r', 'p', 's'])

    def is_win(self):
        if (self.user == 'r' and self.computer == 's') or (self.user == 'p' and self.computer == 'r') or (self.user == 's' and self.computer == 'p'): 
            return True

    def result(self):
        if self.user == self.computer: return f'{Fore.YELLOW}Its a tie!'
        if self.is_win(): return f'{Fore.GREEN}you won'
        return f'{Fore.RED}you lost'

game = RockPaperScissors()
print(game.result())