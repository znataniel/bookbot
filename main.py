def letter_count(book_str):
    letters = {}
    book_str = book_str.lower()
    for char in book_str:
        if (char in letters):
            letters[char] += 1
        else:
            letters[char] = 1

    return letters


def word_count(book_str):
    words = book_str.split()
    return len(words)


def read_book_to_str(book_path):
    with open(book_path) as book:
        return book.read()


def main():
    book_in_str = read_book_to_str("./books/frankenstein.txt")
    wc = word_count(book_in_str)
    print(f"Words in book: {wc}")
    lc_dict = letter_count(book_in_str)
    print(lc_dict)


main()
