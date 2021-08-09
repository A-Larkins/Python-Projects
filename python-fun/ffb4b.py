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

fantasy_points = []
for player in players:
    points_scored = player.get('catches', 0) + player.get('rec_yds', 0) * .1 + player.get('td', 0) * 6
    fantasy_points.append(points_scored)

print(sum(fantasy_points) / len(fantasy_points))