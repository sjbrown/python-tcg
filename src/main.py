#! /usr/bin/env python

import os
from datetime import datetime

import core
import objects

def main():
    now_str = datetime.now().strftime('%Y-%m-%d-%H-%M')
    user = objects.User()
    game = objects.Game(user, 'Game-%s' % now_str)

    game.make_square_deck('../sample/deck_a')
    game.make_poker_deck('../sample/deck_b')
    game.make_booklet('../sample/booklet_a')

if __name__ == '__main__':
    main()
