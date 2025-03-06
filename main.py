from stats import count_words_stats
from stats import count_chars_stats
from stats import dict_to_list_stats
from stats import sort_on_stats
import pprint
import sys

def main_old():
    print("--- Begin report of books/frankenstein.txt ---")
    words = count_words_old()
    print(f"{words} words found in the document\n\n")
    result = count_chars_old()
    result = dict_to_list(result)
    result.sort(key=sort_on, reverse=True)
    for item in result:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words_stats(f"{book_path}")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = count_chars_stats(f"{book_path}")
    result = dict_to_list_stats(num_chars)
    result.sort(key=sort_on_stats, reverse=True)
    for item in result:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def dict_to_list(dict):
    dict_list = [
        {"char":char, "num":count}
        for char, count in dict.items()
    ]
    return dict_list

def dict_to_list_debug(dict):
    print("Original dictionary:", dict)
    print("Result of dict.items():", dict.items())
    dict_list = []
    for char, count in dict.items():
        new_item = {"char": char, "num": count}
        dict_list.append(new_item)
        pprint.pprint(dict_list)
    return dict_list

def sort_on(item):
    return item ["num"]
    
def print_contents():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words_old():
    words = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
    return words

def count_chars_old():
    chars_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for char in file_contents:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict

if __name__ == "__main__":
    main()