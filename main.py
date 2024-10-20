def main():
    report('books/frankenstein.txt')

def word_count(filepath):
    file = open(filepath, 'r')
    text = file.read()
    word_count = len(text.split())
    file.close()
    return word_count

def char_count(filepath):
    char_count = {}
    file = open(filepath, 'r')
    text = file.read()
    for char in text:
        lowered = char.lower()
        if lowered == ' ':
            continue
        if lowered == '\n':
            continue
        elif lowered in char_count:
            char_count[lowered] = char_count[lowered] + 1
        else:
            char_count[lowered] = 1

    return char_count

def report(filepath):
    x = word_count(filepath)
    y = char_count(filepath)
    sorted_chars = sorted(y.items(), key=lambda x:x[1], reverse=True)

    print(f"--- Begin report of {filepath} ---")
    print(f"{x} words found in the document\n")
    for i in sorted_chars:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

main()
