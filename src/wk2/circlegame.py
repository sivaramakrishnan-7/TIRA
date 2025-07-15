def find_order(n):
    if n == 0:
        return []
    
    players = [_ for _ in range(1,n+1)]
    leaving_order = []
    current_player = 0
    for _ in range(n):
        num_players_left = len(players)

        idx_to_remove = (current_player + 1) % (num_players_left)
        removed_player = players.pop(idx_to_remove)
        leaving_order.append(removed_player)

        current_player = idx_to_remove

    return leaving_order

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]