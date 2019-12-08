import json
from collections import Counter

questions = [0, 2, 4, 6, 8, 10]
with open('results.json') as json_file:
    data = json.load(json_file)
    for idx in questions:
        question = data[idx]
        print(question['text'])

        print(Counter(question['answers']))
