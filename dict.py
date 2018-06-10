import json
from difflib import get_close_matches
data = json.load(open("dict-data.json"))


def dict_main(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        choice = input("You mean %s? Y|y or N|n : " % get_close_matches(word, data.keys())[0])
        if choice == "Y" or "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word not exits"

    else:
        return "word not exits"


word = input("enter word: ")

output = dict_main(word)
if type(output) == list:
    for i in output:
        print("-->"+i)

else:
    print(output)

