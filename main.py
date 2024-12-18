def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)
    

def get_word_count(text):
    return len(text.split())

def sort_char_dicts(dict):
    return dict["count"]

def get_char_count(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

def get_sorted_char_count(text):
    char_dict = get_char_count(text)
    dicts = []
    for char in char_dict:
        dicts.append({"name": char, "count": char_dict[char]})
    
    sorted_dicts = dicts.sort(reverse=True, key=sort_char_dicts)
    return dicts

def print_report(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        print(f'--- Begin report of {book_path} ---')
        print(f'{get_word_count(file_contents)} words found in the document\n')
        
        char_counts = get_sorted_char_count(file_contents)
        for char_dict in char_counts:
            print(f'The \'{char_dict["name"]}\' character was found {char_dict["count"]} times') 
        print("--- End report ---")

main()