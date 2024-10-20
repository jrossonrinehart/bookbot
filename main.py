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
    text = text.lower()
    for char in text:
        if char == ' ':
            continue
        elif char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 0

    return char_count

def report(filepath):
    x = word_count(filepath)
    y = char_count(filepath)
    sorted_chars = sorted(y.items(), key=lambda x:x[1])

    print(f"--- Begin report of {filepath} ---")

main()
