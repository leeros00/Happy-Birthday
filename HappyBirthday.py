# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 12:40:01 2022

@author: ltlee
"""

from __future__ import print_function
import sys

try:
    import simpleaudio as sa
    import numpy as np
    import webbrowser
    
except ImportError:
    import pip
    pip.main(['install', '--user', 'simpleaudio'])
    import simpleaudio as sa
    pip.main(['install', '--user', 'numpy'])
    import numpy as np
    pip.main(['install', '--user', 'webbrowser'])
    import webbrowser


def sound(x, z):
    frequency = x
    fs = 44100 # 44100 samples per second
    seconds = z

    t = np.linspace(0, seconds, int(seconds*fs), False)

    note = np.sin(frequency*t*2*np.pi)

    audio = note*(2**15 - 1)/np.max(np.abs(note))

    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, fs)

    return play_obj.wait_done()

sound(264, 0.250)
print('Ha', end ='')
print('ppy ', end = '')
sound(264, 0.250)
print('birth', end = '')
sound(297, 1)
print('day ', end = '')
sound(264, 1)
print('to ', end = '')
sound(352, 1)
print('you')
sound(330, 2)

print('Ha', end = '')
sound(264, 0.250)   
print('ppy ', end = '')
sound(264, 0.2500)
print('birth', end = '')
sound(297, 1)
print('day ', end = '')
sound(264, 1)
print('to ', end = '')
sound(396, 1)
print('you')
sound(352, 2)

print('Ha', end = '')
sound(264, 0.250)
print('ppy ', end = '')
sound(264, 0.50)
print('birth', end = '')
sound(523, 1)
print('day ', end = '')
sound(440, 1)
print('dear ', end = '')
sound(350, 1)
print('[Na-', end = '')
sound(330, 1)
print('me]')
sound(294, 1)
print("")
    
print('Ha', end = '')
sound(466, .250)
print('ppy ', end = '')
sound(466, .250)
print('birth', end = '')
sound(440, 1)
print('day ', end = '')
sound(352, 1)
print('to ', end = '')
sound(396, 1)
print('you')
sound(352, 2)
print("")

