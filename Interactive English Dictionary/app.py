import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def findWord(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        qn = input("Do you mean %s instead? Answer yes or no !!  " % get_close_matches(w,data.keys())[0])
        if qn == "yes":
            return data[get_close_matches(w,data.keys())[0]]
        elif qn == "no":
            return "The Word Doesnt exist"
        else:
            return "Please give a  valid input"
    else:
        return "The Word doesnt exist"

word = input("Enter the Word to search : ")

output = findWord(word)

if type(output) == list:
    for val in output:
        print(val)
else:
    print(output)