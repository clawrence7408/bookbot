import sys
from stats import count_words, count_characters, sort_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    char_counts = sort_counts(count_characters(book_text))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in char_counts:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["num"]}")
    print("============= END ===============")


if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()