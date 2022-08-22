import candy_service as main

def init():
    global candyes_count
    candyes_count = 100
    global max_value
    max_value = 28
    global player_num
    player_num = main.randomize_player()
    global last_step
    last_step = 0

def whose_move() -> str:
    if player_num == 0:
        return "Ваш ход"
    else:
        return "Ход бота"

def bot_step() -> str:
    global candyes_count, max_value, player_num, last_step
    bot_value = main.bot_step(candyes_count, max_value, last_step)
    candyes_count -= bot_value
    if candyes_count > 0:
        player_num = 0
    return f"Бот взял {bot_value} конфет\nОсталось {candyes_count} конфет"

def player_step(value) -> str:
    global candyes_count, max_value, player_num, last_step
    if value > max_value:
        return f"Слишком много конфет, можно взять максимум {max_value}"
    else:
        candyes_count -= value
    if candyes_count > 0:
        last_step = value
        player_num = 1
    return f"Вы взяли {value} конфет\nОсталось {candyes_count} конфет"

def restart() -> None:
    init()

init()