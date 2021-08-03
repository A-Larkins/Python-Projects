# Chapter 2

players = [{
    'name': 'Derrick Henry',
    'rushing_yards': 2027,
    'rushing_attempts': 378
  }, 
  { 
    'name': 'Dalvin Cook',
    'rushing_yards': 1557,
    'rushing_attempts': 312
  },
  {
    'name': 'Jonathan Taylor',
    'rushing_yards': 1169,
    'rushing_attempts': 232
  }
]

for player in players:
  name = player['name']
  rush_yards = player['rushing_yards']
  rush_attempts = player['rushing_attempts']
  yards_per_rush = rush_yards/rush_attempts
  print(name + ': ' + str(yards_per_rush))  

