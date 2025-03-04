import sys
from stats import count_words, count_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    with open(path) as f:
        file_contents = f.read()
        words_count = count_words(file_contents)
        chars = count_characters(file_contents)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")

        for char in chars:
            print(f"{char}: {chars[char]}")

        print("============= END ===============")


main()
