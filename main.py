import token_bot as t
import markups as m
import telebot
import candy_controller as candy
import bullcow_controller as bullcow

token = t.get_token()
bot = telebot.TeleBot(token)

global started_candy

@bot.message_handler(commands=["start", 'go'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет')
    msg = bot.send_message(chat_id, 'Во что поиграем?', 
    reply_markup= m.source_markup)
    bot.register_next_step_handler(msg, askAction)

def askAction(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text == "игра в конфеты":
        bot.send_message(chat_id, "Открываю игру в конфеты")
        candy.restart()
        if candy.player_num == 0: #Ход игрока
            msg = bot.send_message(chat_id, "Первый ход ваш")
            bot.register_next_step_handler(msg, candyes_game)
        else: #Ход бота
            bot.send_message(chat_id, "Первый ход бота")
            reply = candy.bot_step()
            msg = bot.send_message(chat_id, reply)
            bot.register_next_step_handler(msg, candyes_game)

    elif text == "быки и коровы":
        bullcow.what_is_word()
        bot.send_message(chat_id, 'Открываю игру "Быки и коровы"')
        msg = bot.send_message(chat_id, bullcow.what_is_word())
        bot.register_next_step_handler(msg, bull_cow_game)

def candyes_game(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit(): #Проверяем, введено ли число
        msg = bot.send_message(chat_id, "Пожалуйста, введи число!")
        bot.register_next_step_handler(msg, candyes_game)
    if candy.candyes_count > 0:
        bot.send_message(chat_id, candy.whose_move())
        if candy.player_num == 0: #Ход игрока
            reply = candy.player_step(int(text))
            bot.send_message(chat_id, reply)
            bot.send_message(chat_id, candy.whose_move())
            reply = candy.bot_step()
        else: #Ход бота
            reply = candy.bot_step()
        msg = bot.send_message(chat_id, reply)
        if candy.candyes_count <= 0:
            if candy.player_num == 0:
                msg = bot.send_message(chat_id, "Вы победили!")
            else:
                msg = bot.send_message(chat_id, "Победил бот. В следующий раз повезет!", reply_markup=m.source_markup)
            candy.restart()
            bot.register_next_step_handler(msg, askAction)
        bot.register_next_step_handler(msg, candyes_game)

def bull_cow_game(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if bullcow.check_len(text):
        if bullcow.check_correct_word(text):
            msg = bot.send_message(chat_id, "Ура, ты угадал слово")
            bot.register_next_step_handler(msg, askAction)
        else:
            msg = bot.send_message(chat_id, bullcow.ask_cow_bulls(text))
            bot.register_next_step_handler(msg, bull_cow_game)
    else:
        bot.send_message(chat_id, "Количество символов не совпадает с загаданным словом")
        msg = bot.send_message(chat_id, bullcow.get_len_curr_word())
        bot.register_next_step_handler(msg, bull_cow_game)

bot.polling()