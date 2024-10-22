import random
import art
from game_data import data

game_status = True
score = 0


def compare (person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return 'a'
    else: return 'b'

while game_status:
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    else:
        celebrity1 = random.choice(data)
        celebrity2 = random.choice(data)
    print(f"Compare A: {celebrity1['name']}, a {celebrity1['description']}, from {celebrity1['country']}.")
    print(art.vs)
    print(f"Compare B: {celebrity2['name']}, a {celebrity2['description']}, from {celebrity2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
    if choice == compare(celebrity1,celebrity2):
        celebrity1 = celebrity2
        celebrity2 = random.choice(data)
        score += 1
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        score = 0
        keep_play = input("Would you like play again? Type 'y' or 'n'.\n").lower()
        if keep_play == 'n':
            game_status = False