import json

data = json.load(open("data.json"))
def findWord(w):
    if w in data:
        return data[w]
    else:
        return "Please give a  valid input"

word = "rain"
print(findWord(word))