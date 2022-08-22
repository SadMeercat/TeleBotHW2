from random import randint as r

def select_word():
    with open("words", 'r', encoding='utf-8') as data:
        data = data.readlines()
    main_word = data[r(0,len(data)-1)].replace("\n", "")
    return main_word
    
def calc_symbols(inpt_str: str, curr_word: str) -> list:
    count_bull = 0
    count_cow = 0
    index_curr = 0
    index_inpt = 0
    for i in inpt_str: #Перебираем символы входящего слова
        for j in curr_word: #перебираем символы загаданного слова
            if i == j:
                if index_curr == index_inpt:
                    count_bull += 1
                else:
                    count_cow += 1
            index_curr += 1
        index_inpt += 1
        index_curr = 0
    return [count_bull, count_cow]