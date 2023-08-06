import pygame


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
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(notchIndex-ringIndex) % 26]

    def draw(self, screen, x, y, w, h, font):
        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        for i in range(26):
            # left column
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/4, y+(i+1)*h/27))
            # highlight top letter
            if i == 0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=5)

            # highlight notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "white", text_box, border_radius=5)

            screen.blit(letter, text_box)

            # right column
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+3*w/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)
