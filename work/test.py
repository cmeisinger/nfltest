#!python

import nflgame

games = nflgame.games(2015, week=[8, 9, 10, 11, 12, 13, 14, 15, 16])
players = nflgame.combine(games)
for p in players.rushing().sort('rushing_yds').limit(10):
        msg = '%s %d carries for %d yards and %d TDs'
        print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)
