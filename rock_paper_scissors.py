import random

human_score = 0
computer_score = 0

choices = ['rock', 'paper', 'scissors']

while True:
    human_choice = input('Choose Rock, Paper, Scissors or quit: ').lower()
    if human_choice.lower() == 'quit':
        break

    computer_choice = random.randint(0, 2)  # 0:- rock, 1:- paper, 2:- scissors
    computer_pick = choices[computer_choice]
    print(f'Computer has chosen {computer_pick}.')

    if human_choice == 'rock' and computer_pick == 'scissors':
        print('Good choice bro!')
        human_score += 1
        continue
    if human_choice == 'paper' and computer_pick == 'rock':
        print('Good choice bro!')
        human_score += 1
        continue
    if human_choice == 'scissors' and computer_pick == 'paper':
        print('Good choice bro!')
        human_score += 1
        continue
    if human_choice == computer_pick:
        print("It's a tie")
        continue
    else:
        print('bad choice bro!')
        computer_score += 1

print(f"You've won {human_score} times")
print(f'Computer has won {computer_score} times')

if human_score > computer_score:
    print("You've outsmarted the computer boi!!")
elif human_score == computer_score:
    print("It's a tie")
else:
    print("Your bad luck will never fade!")
print('Adios!')