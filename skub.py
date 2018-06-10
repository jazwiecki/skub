# -*- coding: utf-8 -*-
"""
Python library class for translating alpha ascii to other unicode fonts
"""

import collections
import string

Typeface = collections.namedtuple('Typeface', str.join(' ', string.ascii_letters))

fraktur_ref = '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅'

typefaces = {'fraktur' : Typeface(*fraktur_ref)}

def transform(text, typeface):
    if typeface in typefaces:
        return str.join('', [getattr(typefaces[typeface], char, char) for char in text])
    else:
        known_type_faces = str.join(',', [t for t in typefaces.keys()])
        return "Couldn't find {}, here is a list of available typefaces: {}".format(typeface, known_type_faces)
