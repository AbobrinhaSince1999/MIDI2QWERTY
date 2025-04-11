import keyboard as kb

OFFSET_MAP = [24, 36, 48, 60, 72, 84, 96]

# Maps MIDI note offsets (after transposing) to keyboard keys
KEY_MAP = [
    # 1st Octave
    lambda: kb.press_and_release('1'),
    lambda: kb.press_and_release('shift+1'),
    lambda: kb.press_and_release('2'),
    lambda: kb.press_and_release('shift+2'),
    lambda: kb.press_and_release('3'),
    lambda: kb.press_and_release('4'),
    lambda: kb.press_and_release('shift+4'),
    lambda: kb.press_and_release('5'),
    lambda: kb.press_and_release('shift+5'),
    lambda: kb.press_and_release('6'),
    lambda: kb.press_and_release('shift+6'),
    lambda: kb.press_and_release('shift+7'),
    
    # 2nd Octave
    lambda: kb.press_and_release('8'),
    lambda: kb.press_and_release('shift+8'),
    lambda: kb.press_and_release('9'),
    lambda: kb.press_and_release('shift+9'),
    lambda: kb.press_and_release('0'),
    lambda: kb.press_and_release('q'),
    lambda: kb.press_and_release('shift+q'),
    lambda: kb.press_and_release('w'),
    lambda: kb.press_and_release('shift+w'),
    lambda: kb.press_and_release('e'),
    lambda: kb.press_and_release('shift+e'),
    lambda: kb.press_and_release('r'),

    # 3rd Octave
    lambda: kb.press_and_release('t'),
    lambda: kb.press_and_release('shift+t'),
    lambda: kb.press_and_release('y'),
    lambda: kb.press_and_release('shift+y'),
    lambda: kb.press_and_release('u'),
    lambda: kb.press_and_release('i'),
    lambda: kb.press_and_release('shift+i'),
    lambda: kb.press_and_release('o'),
    lambda: kb.press_and_release('shift+o'),
    lambda: kb.press_and_release('p'),
    lambda: kb.press_and_release('shift+p'),
    lambda: kb.press_and_release('a'),

    # 4th Octave
    lambda: kb.press_and_release('s'),
    lambda: kb.press_and_release('shift+s'),
    lambda: kb.press_and_release('d'),
    lambda: kb.press_and_release('shift+d'),
    lambda: kb.press_and_release('f'),
    lambda: kb.press_and_release('g'),
    lambda: kb.press_and_release('shift+g'),
    lambda: kb.press_and_release('h'),
    lambda: kb.press_and_release('shift+h'),
    lambda: kb.press_and_release('j'),
    lambda: kb.press_and_release('shift+j'),
    lambda: kb.press_and_release('k'),

    # 5th Octave
    lambda: kb.press_and_release('l'),
    lambda: kb.press_and_release('shift+l'),
    lambda: kb.press_and_release('z'),
    lambda: kb.press_and_release('shift+z'),
    lambda: kb.press_and_release('x'),
    lambda: kb.press_and_release('c'),
    lambda: kb.press_and_release('shift+c'),
    lambda: kb.press_and_release('v'),
    lambda: kb.press_and_release('shift+v'),
    lambda: kb.press_and_release('b'),
    lambda: kb.press_and_release('shift+b'),
    lambda: kb.press_and_release('n'),

    # 6th Octave
    lambda: kb.press_and_release('m'),
]
