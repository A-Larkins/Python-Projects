# Chapter 3

from typing import Dict


rbs = [
    {
        'name': 'JD McKissic',
        'targets': 110,
        'catches': 80
    },
    {
        'name': 'Alvin Kamara',
        'targets': 107,
        'catches': 83
    }
]

def get_catch_rate(rb):
    if type(rb) is not dict:
        print('Must be a dict')
        return
    elif rb['targets'] < rb['catches']:
        print('Targets much be greater than catches...')
        return
    return rb['catches'] / rb['targets']

print(get_catch_rate(rbs[1]))    
