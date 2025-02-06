import pprint

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    words = count_words()
    print(f"{words} words found in the document\n\n")
    result = count_chars()
    result = dict_to_list(result)
    result.sort(key=sort_on, reverse=True)
    for item in result:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

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

def count_words():
    words = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
    return words

def count_chars():
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