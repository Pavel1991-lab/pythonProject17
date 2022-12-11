import json


def load_candidates():
    with open('candidates.json','r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_all():
    return load_candidates()



def get_by_pk(pk):
    for cand in load_candidates():
       if cand['pk'] == pk:
           return cand
    return

def get_by_skill(skill):
    a = []
    for i in load_candidates():
        if skill in i['skills'].split(', ') :
            a.append(i)
    return a







