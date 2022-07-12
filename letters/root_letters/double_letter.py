from root_letter import RootLetter


# Двойные буквы соответствуют определенной планете:
class DoubleLetter(RootLetter):

    def __init__(self, planet):

        self.planet = planet