import random
from colorama import init, Fore

init(autoreset=True)

ASCII = {
    'rock': "...ascii art rock...",
    'paper': "...ascii art paper...",
    'scissors': "...ascii art scissors..."
}

def get_choice():
    opts = {'r':'rock','p':'paper','s':'scissors'}
    while True:
        c = input("Choose [r]ock, [p]aper, [s]cissors or 'q' to quit: ").lower()
        if c == 'q': return None
        if c in opts: return opts[c]
        print(Fore.RED + "Invalid input. Try again.")

def check_winner(u, c):
    if u == c: return 'tie'
    wins = {('rock','scissors'), ('paper','rock'), ('scissors','paper')}
    return 'user' if (u, c) in wins else 'comp'

def play_best_of(n):
    u_score = c_score = ties = 0
    for i in range(1, n+1):
        print(Fore.CYAN + f"\nRound {i} of {n}")
        u = get_choice()
        if u is None: return
        c = random.choice(list(ASCII.keys()))
        print(Fore.GREEN + f"You chose:\n{ASCII[u]}")
        print(Fore.MAGENTA + f"Computer chose:\n{ASCII[c]}")
        res = check_winner(u, c)
        if res == 'user':
            print(Fore.GREEN + "You win this round!")
            u_score += 1
        elif res == 'comp':
            print(Fore.RED + "Computer wins this round!")
            c_score += 1
        else:
            print(Fore.YELLOW + "It’s a tie!")
            ties += 1
    print(Fore.CYAN + f"\nFinal Score – You: {u_score}, Computer: {c_score}, Ties: {ties}")
    # Summary
    if u_score > c_score: print(Fore.GREEN + "🎉 You won overall!")
    elif c_score > u_score: print(Fore.RED + "😞 Computer won overall.")
    else: print(Fore.YELLOW + "🏅 Overall tie!")

def main():
    print(Fore.CYAN + "🎮 Rock–Paper–Scissors Game")
    while True:
        rounds = input("Play best of how many? (3,5...) or 'q' to quit: ").lower()
        if rounds == 'q': break
        if rounds.isdigit() and int(rounds) > 0:
            play_best_of(int(rounds))
        else:
            print(Fore.RED + "Enter a valid positive number or 'q'.")

if __name__ == "__main__":
    main()
