import string

class Rotor:
    def __init__(self, wiring, notch, position='A', ring_setting=0):
        self.alphabet = string.ascii_uppercase
        self.wiring = wiring
        self.notch = notch
        self.position = position
        self.ring_setting = ring_setting
        self.initial_position = position

    def rotate(self):
        self.position = self.alphabet[(self.alphabet.index(self.position) + 1) % 26]

    def at_notch(self):
        return self.position == self.notch

    def encrypt_forward(self, char):
        offset = (self.alphabet.index(char) + self.alphabet.index(self.position) - self.ring_setting) % 26
        return self.alphabet[(self.alphabet.index(self.wiring[offset]) - self.alphabet.index(self.position) + self.ring_setting) % 26]

    def encrypt_backward(self, char):
        offset = (self.alphabet.index(char) + self.alphabet.index(self.position) - self.ring_setting) % 26
        index = (self.wiring.index(self.alphabet[offset]) - self.alphabet.index(self.position) + self.ring_setting) % 26
        return self.alphabet[index]

    def reset_position(self):
        self.position = self.initial_position
