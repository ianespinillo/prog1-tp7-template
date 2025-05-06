def index_of_by_index(word, list, index):
    if index < 0 or index >= len(list):
        return -1
    for i in range(index, len(list)):
        if list[i] == word:
            return i
    return -1
    


def index_of_empty(list):
    for i in range(len(list)):
        if list[i] == "":
            return i
    return -1


def index_of(word, list):
    if word in list:
        return list.index(word)
    else:
        return -1


def put(word, list):
    if "" in list:
        idx = list.index("")
        list[idx] = word
        return idx
    else:
        return -1


def remove(word, list):
    eliminated = 0
    for i in range(len(list)):
        if (list[i] == word):
            list[i]=""
            eliminated+=1
    return eliminated
