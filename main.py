import sys
import berserk
import chess

import Game

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.clients.Client(session)
board = berserk.clients.Board(session)

# Gets your account data, e.g ["id"], ["username"]
account_data = client.account.get()
player_id = account_data["id"]

# Welcome text
print("Welcome to Lichess!\n")
print("What kind of chess do you want to play?")
print("1. Rapid (10+0)\n2. Classical (30+0)")
num = input("Enter 1 or 2: ")
time = 0

if num=="1":
    time=10
elif num=="2":
    time=30
else:
    # This needs improvement, something like a while/for loop
    print("Something went wrong, please enter the lichess command again.")
    sys.exit()

board.seek(time, 0)

is_polite = True
for event in board.stream_incoming_events():
    if event['type'] == 'challenge':
        print("Challenge time!!!")

        # Accepts the challenge, mainly used for testing
        game_id = event['challenge']['id']
        board.accept_challenge(game_id)

        # Post message in chat
        #board.post_message(game_id, "Hello noob!")
    elif event['type'] == 'gameStart':
        game = Game.Game(board, event['game']['id'], player_id)
        game.start()