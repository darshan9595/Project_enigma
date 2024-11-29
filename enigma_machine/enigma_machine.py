from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

import string

class EnigmaMachine:
    def __init__(self, rotors, plugboard, reflector):
        self.rotors = rotors
        self.plugboard = plugboard
        self.reflector = reflector

    def rotate_rotors(self):
        # Toujours faire tourner le premier rotor
        self.rotors[0].rotate()

        # Gérer le double stepping
        if len(self.rotors) > 1:
            # Si le premier rotor est à la position de "notch", tourner également le deuxième rotor
            if self.rotors[0].at_notch():
                self.rotors[1].rotate()

            # Si le deuxième rotor est à la position de "notch", tourner également le troisième rotor
            #cela implique que le deuxième rotor fait double stepping lors qu'il est à la position de "notch"
            if len(self.rotors) > 2 and self.rotors[1].at_notch():
                self.rotors[2].rotate()

    def encrypt(self, message):
        encrypted_message = []
        for char in message:
            if char in string.ascii_uppercase:
                self.rotate_rotors()
                char = self.plugboard.swap(char)
                for rotor in self.rotors:
                    char = rotor.encrypt_forward(char)
                char = self.reflector.reflect(char)
                for rotor in reversed(self.rotors):
                    char = rotor.encrypt_backward(char)
                char = self.plugboard.swap(char)
            encrypted_message.append(char)
        return ''.join(encrypted_message)

    def reset_rotors(self):
        for rotor in self.rotors:
            rotor.reset_position()
