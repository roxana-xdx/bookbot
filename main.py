def main():
    #get the text
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    #count the number of words
    num_words = get_num_words(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    #create a dictionary: key = character, value = number of occurences
    characters_dictionary = get_character_count(text)
    
    #create a list of dictionaries, where each dictionary has the key and value for one char
    characters_list = dict_to_list(characters_dictionary)
    
    #sort the list starting with the char that has most occurences
    characters_list.sort(reverse=True, key=sort_on)

    #print each letter with its number of occurences
    for entry in characters_list:
        letter = entry["letter"]
        num = entry["num"]
        print(f"The {letter} character was found {num} times")
    print("--- End report ---")

#returns the number of words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

#returns the content of a file (book)
def get_book_text(path):
    with open(path) as f:
        return f.read()

#returns a dictionary with key=char, value=number of occurences
def get_character_count(text):
    dict = {}
    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

#turns a dictionary into a list of dictionaries
def dict_to_list(dictionary):
    list = []
    for key in dictionary:
        if key.isalpha():
            new_dict = {"letter": key, "num": dictionary[key]}
            list.append(new_dict)
    return list

#this is how the .sort() method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

main()