"""Module providing functions to calculate statistics given a book"""


def get_book_word_count(book_text):
    """Returns the word count of a book

    Args:
        book_text (str): The text of the book

    Returns:
        int: The word count
    """
    return len(book_text.split())


def get_book_char_count(book_text):
    """Returns the character count of a book as a dictionary

    Args:
        book_text (str): The text of the book

    Returns:
        dict: The character count
    """
    char_count_dict = {}
    for char in book_text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict


def sort_char_count(char_count_dict):
    """Sorts a character count dictionary

    Args:
        char_count_dict (dict): The character count dictionary

    Returns:
        list: The sorted character count
    """
    new_list = []

    def sorter(items):
        return items["num"]

    for char in char_count_dict:
        new_list.append({"char": char, "num": char_count_dict[char]})

    new_list.sort(key=sorter, reverse=True)

    return new_list
