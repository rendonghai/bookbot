import sys

from stats import get_book_text, get_num_words, get_chars_dict, chars_dict_to_sorted_list


def print_report(book_path, num_words, chars_sorted):
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {book_path}...")
      print("----------- Word Count ----------")
      print(f"Found {num_words} total words")
      print("--------- Character Count -------")
      for c, n in chars_sorted:
                if not c.isalpha():
                              continue
                          print(f"{c}: {n}")
            print("============= END ===============")


def main():
      if len(sys.argv) < 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
            book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_sorted = chars_dict_to_sorted_list(get_chars_dict(text))
    print_report(book_path, num_words, chars_sorted)


main()

