rbs = [
    {
        'name': 'Derrick Henry',
        'rushing_yrds': 2027,
        'rushing_tds': 17,
        'receptions': 19,
        'receiving_yrds': 114,
        'receiving_tds': 0
    },
    {
        'name': 'Dalvin Cook',
        'rushing_yrds': 1557,
        'rushing_tds': 16,
        'receptions': 44,
        'receiving_yrds': 361,
        'receiving_tds': 1
    },
    {
        'name': 'Jonathan Taylor',
        'rushing_yrds': 1169,
        'rushing_tds': 11,
        'receptions': 36,
        'receiving_yrds': 299,
        'receiving_tds': 1
    }
]

def calculate_fantasy_points(rb, ppr=False):
    total_yards = rb['rushing_yrds'] + rb['receiving_yrds']
    total_tds = rb['rushing_tds'] + rb['receiving_tds']
    catches = rb['receptions']
    if ppr:
        points = total_yards * 0.1 + total_tds * 6 + catches
        return points
    else: 
        points = total_yards * 0.1 + total_tds * 6
        return points
    

dh = rbs[0]
print(calculate_fantasy_points(dh))

dc = rbs[1]
print(calculate_fantasy_points(dc, ppr=True))