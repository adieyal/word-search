word_search = [
    "GARGANTAESKCOUBMSW",
    "SJGSTMYWSTEEBALEFV",
    "UOACOBQMPFOTREIDAH",
    "RRDDINJSALERNPTRZV",
    "THOECNQWLFIGSEJWEL",
    "ALLIDOREDGUODXICBA",
    "ETNERFULAALPLEXDAB",
    "OTNFRCGOREJAISWGCI",
    "BQGWDKOBDFAVAEZCYO",
    "HAHMYJKSXMMONTRTUS",
    "BOWKOGOSWGNTTOXNWQ",
    "HNMSSDHXDQGCTSPWAA",
    "WPYBEPZRPXKNQKISLJ",
    "OLEDRIAOKTVIPXEOKM",
    "WNULRODRVNBWKTSNAI",
    "FVIAOFSUXTCAZSTAJZ",
    "SYNPIWHJOUYIHXVMJN",
    "PBRAZOSRAZCBNUDSLO",
]

words_to_find = [
    "BOCA",
    "RODILLAS",
    "CUELLO",
    "LABIOS",
    "PIERNAS",
    "PELO",
    "OREJA",
    "FRENTE",
    "PIES",
    "OJOS",
    "NARIZ",
    "HOMBROS",
    "DIENTES",
    "LENGUA",
    "GARGANTA",
    "MANOS",
    "CABEZA",
    "ESPALDA",
    "BARRIGA",
    "DEDOS",
    "BRAZOS",
    "DEDOSDELOSPIES",
]


def search_left_to_right(word_search, row, col, word):
    if col + len(word) > len(word_search[row]):
        return False
    for i in range(len(word)):
        if word[i] != word_search[row][col + i]:
            return False
    return True


def search_right_to_left(word_search, row, col, word):
    for i in range(len(word)):
        if word[i] != word_search[row][col - i]:
            return False
    return True


def search_top_to_bottom(word_search, row, col, word):
    if row + len(word) > len(word_search):
        return False
    for i in range(len(word)):
        if word[i] != word_search[row + i][col]:
            return False
    return True


def search_bottom_to_top(word_search, row, col, word):
    for i in range(len(word)):
        if word[i] != word_search[row - i][col]:
            return False
    return True


def search_diagonal_left_to_right(word_search, row, col, word):
    if col - len(word) < 0:
        return False

    if row + len(word) > len(word_search):
        return False

    for i in range(len(word)):
        if word[i] != word_search[row + i][col - i]:
            return False
    return True


def search_diagonal_right_to_left(word_search, row, col, word):
    if col + len(word) > len(word_search[row]):
        return False

    if row - len(word) < 0:
        return False

    if row + len(word) > len(word_search):
        return False

    for i in range(len(word)):
        if word[i] != word_search[row + i][col + i]:
            return False
    return True


# Write a function to search for words in the words_to_find list in the word_search list
# Search left to right
# Search top to bottom
# Search diagonally
def search(word_search, words_to_find):
    for word in words_to_find:
        for row in range(len(word_search)):
            for col in range(len(word_search[row])):
                if search_left_to_right(word_search, row, col, word):
                    print(f"Found LEFT TO RIGHT {word} at {row}, {col}")
                if search_left_to_right(word_search, row, col, word[::-1]):
                    print(f"Found LEFT TO RIGHT2 {word} at {row}, {col}")
                # if search_right_to_left(word_search, row, col, word):
                #     print(f"Found RIGHT TO LEFT {word} at {row}, {col}")
                if search_top_to_bottom(word_search, row, col, word):
                    print(f"Found TOP TO BOTTOM {word} at {row}, {col}")
                if search_top_to_bottom(word_search, row, col, word[::-1]):
                    print(f"Found TOP TO BOTTOM2 {word} at {row}, {col}")
                # if search_bottom_to_top(word_search, row, col, word):
                #     print(f"Found BOTTOM TO TOP {word} at {row}, {col}")
                if search_diagonal_left_to_right(word_search, row, col, word):
                    print(f"Found LEFT TO RIGHT DIAGONAL {word} at {row}, {col}")
                if search_diagonal_left_to_right(word_search, row, col, word[::-1]):
                    print(
                        f"Found LEFT TO RIGHT DIAGONAL BACKWARDS {word} at {row}, {col}"
                    )
                if search_diagonal_right_to_left(word_search, row, col, word):
                    print(f"Found RIGHT TO LEFT DIAGONAL {word} at {row}, {col}")
                if search_diagonal_right_to_left(word_search, row, col, word[::-1]):
                    print(
                        f"Found RIGHT TO LEFT DIAGONAL BACKWARDS {word} at {row}, {col}"
                    )


search(word_search, words_to_find)
