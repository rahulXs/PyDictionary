import json
data = json.load(open("dict-data.json"))


def dict_main(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "word not exits"


word = input("enter word: ")

output = dict_main(word)
if type(output) == list:
    for i in output:
        print("-->"+i)

else:
    print(output)

