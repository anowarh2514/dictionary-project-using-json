import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        match = input("Did you mean '%s' instead of? Enter Y if yes , Enter N if no: " %get_close_matches(w,data.keys())[0])
        if match == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif match == "N":
            new_match = input("Did you mean '%s' instead of? Enter Y if yes , Enter N if no: " % get_close_matches(w, data.keys())[1])
            if new_match == "Y":
                return data[get_close_matches(w, data.keys())[1]]
            elif new_match == "N":
                other_match = input("Did you mean '%s' instead of? Enter Y if yes , Enter N if no: " % get_close_matches(w, data.keys())[2])
                if other_match == "Y":
                    return data[get_close_matches(w, data.keys())[2]]
                elif other_match == "N":
                    return "The word doesn't exist. Please enter a valid word"
                else:
                    return "You input wrong key"
            else:
                return "You input wrong key"
        else:
            return "You input wrong key"
    else:
        return "The word doesn't exist. Please enter a valid word"
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)