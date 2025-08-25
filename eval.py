import json

import re
def retain_digits_commas_newlines(s):
    return re.sub(r'[^0-9,\n]', '', s)

def filter_(input_string):
    output_string = retain_digits_commas_newlines(input_string)

    return output_string

print('==='*15)
print('ARC; Concept-ARC; 1D-ARC; Mini-ARC')
print('==='*15)

print('gpt-4-0613')
for INPUT in ['logs/arc-gpt-4-0613.jsonl']:
    correct=0
    total=0
    with open(INPUT,'r') as f:
        for line in f:
            if len(line.strip())==0:
                continue
            json_obj = json.loads(line.strip())
            if "predict" in json_obj.keys() and json_obj["predict"] != None:
                if json_obj["label"].strip() == filter_(json_obj["predict"].strip()):
                    correct+=1
            total+=1
        print(correct)

for INPUT in ['logs/concept-arc-gpt-4-0613.jsonl','logs/1d-arc-gpt-4-0613.jsonl','logs/mini-arc-gpt-4-0613.jsonl']:
    correct=0
    total=0
    with open(INPUT,'r') as f:
        for line in f:
            if len(line.strip())==0:
                continue
            json_obj = json.loads(line.strip())
            if "predict" in json_obj.keys() and json_obj["predict"] != None:
                if json_obj["label"].strip() == filter_(json_obj["predict"].strip()):
                    correct+=1
            total+=1
        print(correct/total)
print('---'*15)

print('ours')
for INPUT in ['logs/arc-ours.jsonl']:
    correct=0
    total=0
    with open(INPUT,'r') as f:
        for line in f:
            if len(line.strip())==0:
                continue
            json_obj = json.loads(line.strip())
            if "predict" in json_obj.keys() and json_obj["predict"] != None:
                if json_obj["label"].strip() == filter_(json_obj["predict"].strip()):
                    correct+=1
            total+=1
        print(correct)

for INPUT in ['logs/concept-arc-ours.jsonl','logs/1d-arc-ours.jsonl','logs/mini-arc-ours.jsonl']:
    correct=0
    total=0
    with open(INPUT,'r') as f:
        for line in f:
            if len(line.strip())==0:
                continue
            json_obj = json.loads(line.strip())
            if "predict" in json_obj.keys() and json_obj["predict"] != None:
                if json_obj["label"].strip() == filter_(json_obj["predict"].strip()):
                    correct+=1
            total+=1
        print(correct/total)
print('---'*15)