def main():
    path_to_book = "books/frankenstein.txt"
    book_in_str = read_book_to_str(path_to_book)
    wc = word_count(book_in_str)
    lc_dict = letter_count(book_in_str)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{wc} words found in the document.")
    print("\n")

    def sort_on(dict):
        return dict["num"]

    letters = []
    for l in lc_dict:
        if (l.isalpha()):
            letters.append({"name": l, "num": lc_dict[l]})
    letters.sort(reverse=True, key=sort_on)
    for l in letters:
        letter = l["name"]
        num = l["num"]
        print(f"Letter {letter} was found {num} times.")


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


main()
