# Chapter 3

players = [
    {
        'name': 'Stefon Diggs',
        'catches': 127,
        'targets': 166
    },
    {
        'name': 'DeAndre Hopkins',
        'catches': 115,
        'targets': 160
    },
    {
        'name': 'Davante Adams',
        'catches': 115,
        'targets': 149
    },
    {
        'name': 'Darren Waller',
        'catches': 107,
        'targets': 145
    },
    {
        'name': 'Allen Robinson',
        'catches': 102,
        'targets': 151
    }
]

def get_catch_rate(player):
    if type(player) is not dict:
        print('Needs a dict')
        return
    elif player['catches'] > player['targets']:
        print('Targets can\'t be less than catches')
        return
    return player['catches']/player['targets']

print(get_catch_rate(players[0]))


