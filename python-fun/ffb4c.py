players = [
    {
        'name': 'Stefon Diggs',
        'catches': 127,
        'rec_yds': 1535,
        'td': 8
    }, 
    {
        'name': 'Davante Adams',
        'catches': 115,
        'rec_yds': 1374,
        'td': 18
    }
]

def calc_points(player):
    return player.get('catches', 0) + player.get('rec_yds', 0) * .1 + player.get('td', 0) * 6

points = [calc_points(player) for player in players]
print(sum(points)/len(points))
