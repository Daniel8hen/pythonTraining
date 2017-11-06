import json
from difflib import get_close_matches
# The json import is an import which can let you play with JSON
data = json.load(open("data.json"))

def key_to_value(w):
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instaed? Enter 'Y' if yes, 'N' if no: "  % get_close_matches(w, data.keys())[0])
        if (yn.upper() == "Y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif (yn.upper == "N"):
            return "The word is not exist. Please double check it"
        else:
            return "We didn't understand your entry! "
    else:
        return "Word is not exist. Please double check it"

word = input("Enter a word: ")
output = key_to_value(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(item)
