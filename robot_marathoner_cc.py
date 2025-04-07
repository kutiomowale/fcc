#!/usr/bin/env python3

def robot_runner(rt, ft, st, tt):
    """Ensure robot comes second or third in a marathon

    >>> robot_runner("00:30:00", "00:15:00", "00:45:00", "01:15:00")
    True
    >>> robot_runner("01:15:00", "00:15:00", "00:45:00", "01:15:00")
    False
    >>> robot_runner("00:00:01", "00:00:10", "00:01:40", "01:00:00")
    False
    >>> robot_runner("00:10:01", "00:00:10", "00:01:40", "01:00:00")
    True
    """
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
