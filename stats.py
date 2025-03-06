def count_words_stats(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words

def count_chars_stats(path_to_file):
    chars_dict = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for char in file_contents:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict

def dict_to_list_stats(dict):
    dict_list = [
        {"char":char, "num":count}
        for char, count in dict.items()
    ]
    return dict_list

def sort_on_stats(item):
    return item ["num"]