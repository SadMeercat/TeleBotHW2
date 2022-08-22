from random import randint

def randomize_player():
    return randint(0,1)

def bot_step(candy_count, max, last_step) -> int:
    value = max + 1 - last_step

    if candy_count > max and (1 < candy_count / max < 2):
        print(candy_count - (max + 1))
        value = candy_count - (max + 1) 
    if value > candy_count or candy_count <= max:
        value = candy_count
    return value