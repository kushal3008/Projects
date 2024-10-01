import random
player_count = 0
computer_count = 0
tie_count = 0
while True:
    choices = ['rock','paper','scissor']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock paper or scissor?:").lower()
    if player==computer:
        print("Computer: "+computer)
        print("Player: "+player)
        print("It's a Tie!!")
        tie_count += 1
    elif player=="rock":
        if computer=="paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player lost the round")
            computer_count += 1
        if computer=="scissor":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player won the round")
            player_count += 1
    elif player=="paper":
        if computer=="rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player won the round")
            player_count += 1
        if computer=="scissor":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player lost the round")
            computer_count += 1
    elif player=="scissor":
        if computer=="paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player won the round")
            player_count += 1
        if computer=="rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player lost the round")
            computer_count += 1
    print(f"Player: {player_count} wins")
    print(f"Computer: {computer_count} wins")
    print(f"Tie: {tie_count} games are tied")
    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye")