class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"

        vowels = ['a', 'e', 'i', 'o', 'u']
        first_letter = self._phrase[0]

        if first_letter in vowels and self._phrase[-1] == "y":
            return self._phrase + "nay"
        elif first_letter in vowels and self._phrase[-1] in vowels:
            return self._phrase + "yay"



