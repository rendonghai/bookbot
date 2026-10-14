def get_book_text(path):
      with open(path) as f:
                return f.read()


def get_num_words(text):
      return len(text.split())


def get_chars_dict(text):
      chars = {}
      for c in text.lower():
                chars[c] = chars.get(c, 0) + 1
            return chars


def sort_on(item):
      return item[1]


def chars_dict_to_sorted_list(chars_dict):
      pairs = []
    for c in chars_dict:
              pairs.append((c, chars_dict[c]))
          pairs.sort(key=sort_on, reverse=True)
    return pairs

