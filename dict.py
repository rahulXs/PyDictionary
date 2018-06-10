import json
from difflib import get_close_matches
data = json.load(open("dict-data.json"))


def dict_main(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        choice = input("You mean %s? y or n : " % get_close_matches(word, data.keys())[0])
        if choice == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "n":
            return "Word not exits"
        else:
            return "Invalid entry"

    else:
        return "word not exits"


word = input("enter word: ")

output = dict_main(word)
if type(output) == list:
    for i in output:
        print("-->"+i)
else:
    print(output)

