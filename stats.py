def get_book_word_count(book_text):
    return len(book_text.split())


def get_book_char_count(book_text):
    new_char_dict = {}
    for i in range(len(book_text)):
        char = book_text[i].lower()
        if char in new_char_dict:
            new_char_dict[char] += 1
        else:
            new_char_dict[char] = 1
    return new_char_dict


def sort_char_count(char_count_dict):
    new_list = []

    def sorter(items):
        return items["num"]

    for char in char_count_dict:
        new_list.append({"char": char, "num": char_count_dict[char]})

    new_list.sort(key=sorter, reverse=True)

    return new_list
