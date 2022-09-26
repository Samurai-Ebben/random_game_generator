import random as rnd

def rand_genre():
    lst = ['simulation', 'shooter', 'puzzle', 'RPG', 'strategy', 'adventure', 'sports',
           'platformer', 'MOBA' ]
    return rnd.choice(lst)


def rand_theme():
    lst = ['cars', 'survival', 'horror', 'steam punk',
           'stealth', 'apocalypse', 'historic', 'sci-fi']
    return rnd.choice(lst)

print(f'\nthe game will be {rand_genre()} and {rand_theme()}\n')