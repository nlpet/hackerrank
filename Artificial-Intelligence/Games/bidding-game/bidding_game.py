#!/bin/python
def calculate_bid(player,pos,first_moves,second_moves):
    """your logic here"""
    player_one_balance = 100 - sum(first_moves)
    player_two_balance = 100 - sum(second_moves)
    if player == 1:
        if not player_one_balance:
            return 0
        else:
            return player_one_balance / (11 - pos)
    else:
        if not player_two_balance:
            return 0
        else:
            return player_two_balance / (11 - pos)
            
    
    
#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
