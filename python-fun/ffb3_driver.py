from ffb3 import Player

kamara = Player('Alvin Kamara', 'RB', 83, 107, 187, 932)

print('Kamara catch rate: ' + kamara.catch_rate() + '%')
print('Kamara yards per carry: ' + kamara.yards_per_carry())
print('Kamara efficiency: ' + str(kamara.efficiency()))
