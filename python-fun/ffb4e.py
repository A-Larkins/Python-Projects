player_names = ['Derrick Henry', 'Aaron Jones', 'Christian McCaffrey']
receptions = [18, 49, 116]

zip(player_names, receptions)

player_receptions = dict(zip(player_names, receptions))

print(player_receptions)