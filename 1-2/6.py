# Вывести все самые короткие слова через пробел


def solution_1(words):
    min_l = len(words[0])
    for w in words:
        if len(w) < min_l:
            min_l = len(w)

    ans = []
    for w in words:
        if len(w) == min_l:
            ans.append(w)

    return ans

def solution_2(words):
    word_x_len = {}
    for w in words:
        cur_l = len(w)
        if cur_l not in word_x_len:
            word_x_len[cur_l] = []
        word_x_len[cur_l].append(w)

    min_l = min(word_x_len.keys())
    return word_x_len[min_l]


# TODO: тут надо оценить и подумать над стоимостью создания словаря
def solution_3(words):
    min_words = []
    min_l = None
    for w in words:
        cur_l = len(w)
        if not min_l or cur_l < min_l:
            min_words = [w]
            min_l = cur_l
        elif cur_l == min_l:
            min_words.append(w)

    return min_words
# print(solution_1(["a", "aa", "bb", "b"]) == ["a", "b"])
# print(solution_1(["aa", "aa", "bb", "b"]) == ["b"])
# print(solution_1(["a"]) == ["a"])
# print(solution_1(["bb", "a"]) == ["a"])

# print(solution_2(["a", "aa", "bb", "b"]) == ["a", "b"])
# print(solution_2(["aa", "aa", "bb", "b"]) == ["b"])
# print(solution_2(["a"]) == ["a"])
# print(solution_2(["bb", "a"]) == ["a"])


print(solution_3(["a", "aa", "bb", "b"]) == ["a", "b"])
print(solution_3(["aa", "aa", "bb", "b"]) == ["b"])
print(solution_3(["a"]) == ["a"])
print(solution_3(["bb", "a"]) == ["a"])

