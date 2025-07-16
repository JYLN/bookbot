import sys

from stats import get_book_char_count, get_book_word_count, sort_char_count


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        word_count = get_book_word_count(book_text)
        char_count = get_book_char_count(book_text)
        sorted_char_count = sort_char_count(char_count)

        # Print report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for char in sorted_char_count:
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")

        print("============= END ===============")


main()
