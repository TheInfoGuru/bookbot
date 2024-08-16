import re

def create_report(path: str, word_count: int, sorted_list: list) -> str:
    report = ""
    report = f"*** Beginning of the report for {path} ***\n"
    report = report + f"{word_count} words found in the document.\n\n"

    for char, count in sorted_list:
        if not char.isalpha():
            continue
        report = report + f"The character '{char}' was found {count} times.\n"
    return report

def sort_character_counts(character_count: dict) -> list:
    return [ (k, character_count[k]) for k in \
                sorted(character_count, key=character_count.get, reverse=True) ]

#Get the counts for each character in a supplied string
def get_character_counts(text: str):
    character_counts = {} #initialize dic
    for k in text.lower(): #loop through each letter in the text
        try:
            character_counts[k] += 1 #add one to the char count
        except KeyError as e:
            character_counts[k] = 1 #if key doesn't exist yet, set count to 1
    return character_counts

#get the count of the words in a supplied string
def get_word_count(text: str):
    return len(re.findall(r'\S+', text)) #S+ is all words

#get the text of a file at the supplied path
def get_book_text(path: str):
    if not path:
        print("Error: no book path detected.")
        exit(1)
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(path=book_path)
    word_count = get_word_count(text=book_contents)
    character_counts = get_character_counts(text=book_contents)
    sorted_character_count = sort_character_counts(character_count=character_counts)
    report = create_report(path=book_path, word_count=word_count, sorted_list=sorted_character_count)
    print(report)
    exit(0)

main()