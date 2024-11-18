import string

class Plugboard:
    def __init__(self, wiring_pairs):
        self.wiring = self.create_wiring(wiring_pairs)

    def create_wiring(self, wiring_pairs):
        wiring = dict(zip(string.ascii_uppercase, string.ascii_uppercase))
        for pair in wiring_pairs:
            if len(pair) != 2 or not pair.isalpha():
                raise ValueError("Wiring pairs must contain two letters.")
            a, b = pair.upper()
            wiring[a] = b
            wiring[b] = a
        return wiring

    def swap(self, char):
        return self.wiring.get(char, char)
