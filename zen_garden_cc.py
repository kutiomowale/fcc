#!/usr/bin/env python3

def clean_my_zen_garden(s):
    """Clean up my Zen garden

    >>> clean_my_zen_garden("slug spider rock gravel gravel gravel gravel gravel gravel gravel")
    'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'
    >>> clean_my_zen_garden("gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel")
    'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel rock gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel rock gravel gravel'
    >>> clean_my_zen_garden("notgravel gravel notgravel gravel notgravel gravel notgravel gravel notgravel gravel rock rockstar notrock rock rock notrock gravel")
    'gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel rock rock gravel gravel'
    """
    s = s.split()
    r = []
    for word in s:
        if word == 'gravel' or word == 'rock':
            r.append(word)
        else:
            r.append('gravel')
    return ' '.join(r)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
