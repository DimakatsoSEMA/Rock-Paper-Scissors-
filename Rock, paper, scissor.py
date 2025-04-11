#Rock, paper, scissor 
import random

def play():
    print('Ready? Let\'s play Rock, Paper, Scissors!')
    user = input("Choose: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])  # computer makes its choice

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You lose!'

def is_win(player, opponent):
    # Return True if the player beats the opponent
    return (
        (player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')
    )

# Call the game function
print(play())
