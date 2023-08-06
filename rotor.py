class Rotor:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    
    def show(self):
        print(self.left)
        print(self.right)
        print()

    def rotate(self, n=1):
        for i in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotateBack(self, n=1):
        for i in range(n):
            self.left = self.left[-1] + self.left[:25]
            self.right = self.right[-1] + self.right[:25]
    
    def rotateToLetter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ". find(letter)
        self.rotate(n)
    
    def setRing(self, ringIndex):
        self.rotateBack(ringIndex-1)
        notchIndex = "ABCDEFGHIJKLMNOPQRSTUVWXYZ". find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(notchIndex-ringIndex)%26]

