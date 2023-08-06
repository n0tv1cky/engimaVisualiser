class Enigma:
    def __init__(self, re, i, ii, iii, pb, kb):
        self.re = re
        self.i = i
        self.ii = ii
        self.iii = iii
        self.pb = pb
        self.kb = kb

    def setRings(self, rings):
        self.i.setRing(rings[0])
        self.ii.setRing(rings[1])
        self.iii.setRing(rings[2])

    def setKey(self, key):
        self.i.rotateToLetter(key[0])
        self.ii.rotateToLetter(key[1])
        self.iii.rotateToLetter(key[2])

    def encrypt(self, letter):
        if (self.ii.left[0] == self.ii.notch
                and self.iii.left[0] == self.iii.notch):
            self.i.rotate()
            self.ii.rotate()
            self.iii.rotate()
        elif self.ii.left[0] == self.ii.notch:
            self.i.rotate()
            self.ii.rotate()
            self.iii.rotate()
        elif self.iii.left[0] == self.iii.notch:
            self.ii.rotate()
            self.iii.rotate()
        else:
            self.iii.rotate()

        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        signal = self.iii.forward(signal)
        signal = self.ii.forward(signal)
        signal = self.i.forward(signal)
        signal = self.re.reflect(signal)
        signal = self.i.backward(signal)
        signal = self.ii.backward(signal)
        signal = self.iii.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)
        return letter
