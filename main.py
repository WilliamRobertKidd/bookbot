def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count

def count_letters_type():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        letter_dict = {}
        for letter in file_contents:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
        return letter_dict

def book_report(word_count, letter_dict):
    print("-- Book Report --")
    print(f"{word_count} words in book")

    for key in letter_dict:
        if key.isalpha():
            print(f"'{key}' is found {letter_dict[key]} times")
    print("-- Report Complete --")
        
book_report(count_words(), count_letters_type())