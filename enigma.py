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

        path = []
        signal = self.kb.forward(letter)
        path = [signal, signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.iii.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.ii.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.i.forward(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        signal = self.i.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.ii.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.iii.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)
        return path, letter
