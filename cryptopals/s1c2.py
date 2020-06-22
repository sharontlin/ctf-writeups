# fixed xor

import codecs 

def fixed_xor(s1, s2):
    return codecs.encode(''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)), 'hex')

val1 = codecs.decode('1c0111001f010100061a024b53535009181c', 'hex')
val2 = codecs.decode('686974207468652062756c6c277320657965', 'hex')

print(fixed_xor(val1, val2))

# solution: the kid don't play