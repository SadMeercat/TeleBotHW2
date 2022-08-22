import bullcow_service as service

def what_is_word() -> str:
    global current_word
    current_word = service.select_word()
    print(current_word)
    return f"Количество символов загаданного слова: {len(current_word)}"

def ask_cow_bulls(inpt_word: str) -> str:
    global current_word
    my_list = service.calc_symbols(inpt_word, current_word)
    return f"Коров: {my_list[1]}\nБыков: {my_list[0]}"

def check_correct_word(inpt_word: str) -> bool:
    global current_word
    if inpt_word == current_word:
        return True
    else:
        return False

def check_len(inpt_word: str) -> bool:
    global current_word
    if len(inpt_word) == len(current_word):
        return True
    else:
        return False

def get_len_curr_word() -> int:
    global current_word
    return f"Количество символов загаданного слова: {len(current_word)}"