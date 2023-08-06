from keyboards import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# Rotor settings
i = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
ii = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
iii = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
iv = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
v = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

# Reflector settings
a = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
b = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
c = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Plugboard settings
pb = Plugboard(["AB", "CD", "EF"])
kb = Keyboard()

enigma = Enigma(b, iv, ii, i, pb, kb)
# print(enigma.encrypt("A"))
enigma.setKey("CAT")
enigma.setRings((5,26,2))

message = "TESTINGTESTINGTESTINGTESTING"
ciphertext = ""
for letter in message:
    ciphertext += enigma.encrypt(letter)
print(ciphertext)
