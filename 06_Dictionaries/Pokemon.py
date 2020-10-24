from collections import defaultdict
from functools import reduce

players = defaultdict(set)
decks = defaultdict(set)
s = input()
while s:
    if '0' <= s[0] <= '9':
        number, name = s.split(' / ')
        decks[number].add(name)
    else:
        player, number = s.split(' / ')
        players[player].add(number)
    s = input()
    
players_max_decks = []
max_amount = 0
for k, v in players.items():
    deck = set()
    for elem in v:
        deck = deck.union(decks[elem])
    len_deck = len(deck)
    if max_amount < len_deck:
        max_amount = len_deck
        players_max_decks = [k]
    elif max_amount == len_deck:
        players_max_decks.append(k)
            
for player in sorted(players_max_decks):
    print(player)
    