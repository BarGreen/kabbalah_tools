
from importlib.resources import path


class RootLetter():

    # Стандартная буква имеет 5 характеристик: 
    # номер по алфавиту, написание на иврите, название на русском, числовое значение, написание на иврите в конце слова,
    # начало и конец пути в сфирот и слово соответствия духовному пути в материальном мире.
    # extended: соответствующая карта таро Кроули.
    def __init__(self, alphabet_number, hebrew, russian, gematria, end_hebrew, 
                    start_sephirot, end_sephirot, path_word, taro_crowley):

        self.alphabet_number = alphabet_number
        self.hebrew = hebrew
        self.russian = russian
        self.gematria = gematria
        self.end_hebrew = end_hebrew
        self.start_sephirot = start_sephirot
        self.end_sephirot = end_sephirot
        self.path_word = path_word
        self.taro_crowley = taro_crowley
