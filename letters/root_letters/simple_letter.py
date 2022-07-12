from root_letter import RootLetter


# Одинарные буквы соответствуют определенному знаку зодиака:
class SimpleLetter(RootLetter):

    def __init__(self, zodiac):

        self.zodiac = zodiac