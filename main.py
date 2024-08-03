def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num = num_words(text)
    num_chars = get_num_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)
    print(num_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

    