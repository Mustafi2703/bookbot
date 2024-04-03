def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    ch = letter_counts(text)
    chars_sorted_list = sorted_list(ch)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha(): #is an alphabet check
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    #print(text)
    #print(count)

#opening the file
def get_book_text(path):
    with open(path) as f:
        return f.read()
#sorting basis on num
def sort_on(d):
    return d["num"]

def count_words(text):
    words = text.split()
    count = len(words)
    return count

#create are new sorted list from a dictionary
def sorted_list(char_dict):
    l = []
    for i in char_dict:
        l.append({"char" : i , "num" : char_dict[i]})
    l.sort(reverse = True, key = sort_on)
    return l


def letter_counts(text):
    chars = {}
    for i in text:
        l = i.lower()
        if l in chars:
            chars[l] = chars[l] +1
        else:
            chars[l] = 1
    return chars


main()