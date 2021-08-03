# Chapter 4
import math

class Player:
    def __init__ (self, name, pos, catches, targets, rushing_attempts, rushing_yds):
        self.name = name
        self.pos = pos
        self.catches = catches
        self.targets = targets
        self.rushing_attempts = rushing_attempts
        self.rushing_yds = rushing_yds

    def catch_rate(self):
        return str(round(self.catches / self.targets * 100))

    def yards_per_carry(self):
        return str(round(self.rushing_yds / self.rushing_attempts, 2))

    def efficiency(self):
        return {
            'yards_per_carry': self.yards_per_carry(),
            'catch_rate': self.catch_rate()
        }
