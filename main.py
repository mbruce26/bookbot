def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = get_letter_count(text)
    sorted_list = letter_count_to_sorted_list(letter_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document\n")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_letter_count(text):
    letter_counts = {}
    for letter in text.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def sort_on(d):
    return d["num"]


def letter_count_to_sorted_list(letter_counts):
    sorted_list = []
    for ch in letter_counts:
        sorted_list.append({"char": ch, "num": letter_counts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()