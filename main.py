from keyboards import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()
PB = Plugboard(["AR", "GK", "OX"])

'''
letter = "A"
signal = KB.forward(letter)
signal = PB.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = PB.backward(signal)
letter = KB.backward(signal)
print(letter)
'''

I.show()
I.rotateToLetter("G")
I.show()