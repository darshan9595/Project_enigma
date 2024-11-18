import string

class Reflector:
    def __init__(self, wiring):
        if len(wiring) != 26 or len(set(wiring)) != 26:
            raise ValueError("Reflector wiring must contain 26 unique letters.")
        self.wiring = dict(zip(string.ascii_uppercase, wiring))

    def reflect(self, char):
        return self.wiring[char]
