def enumerate_list(list):
    new_list = [i for i in list if i != ""]
    for i in range(len(new_list)):
        new_list[i] = f"{i}. {new_list[i]}"
    return new_list
def enumerate_backwards(list):
    new_list = [i for i in list if i != ""]
    for i in range(len(new_list)-1, -1, -1):
        new_list[i] = f"{i}. {new_list[i][::-1]}"
    return new_list
