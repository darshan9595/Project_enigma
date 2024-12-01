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
        current_index = self.alphabet.index(self.position)
        next_index = (current_index + 1) % 26
        self.position = self.alphabet[next_index]

    def at_notch(self):
        return self.position == self.notch

    def encrypt_forward(self, char):
        offset = (self.alphabet.index(char) + self.alphabet.index(self.position) - self.ring_setting) % 26
        encoded_char = self.wiring[offset]
        result_index = (self.alphabet.index(encoded_char) - self.alphabet.index(self.position) + self.ring_setting) % 26
        return self.alphabet[result_index]


    def encrypt_backward(self, char):
        offset = (self.alphabet.index(char) + self.alphabet.index(self.position) - self.ring_setting) % 26
        decoded_index = self.wiring.index(self.alphabet[offset])
        result_index = (decoded_index - self.alphabet.index(self.position) + self.ring_setting) % 26
        return self.alphabet[result_index]


    def reset_position(self):
        self.position = self.initial_position
