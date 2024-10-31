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

        if self._phrase.__contains__(" "):
            words = self._phrase.split()
            first_word = words[0]
            second_word = words[1]
            if first_word[0] and second_word[0] not in vowels and first_word[1] and second_word[1] in vowels:
                return first_word[1:] + first_letter + "ay" + " " + second_word[1:] + second_word[0] + "ay"

        else:
            if first_letter in vowels and self._phrase[-1] == "y":
                return self._phrase + "nay"
            elif first_letter in vowels and self._phrase[-1] in vowels:
                return self._phrase + "yay"
            elif first_letter in vowels and self._phrase[-1] not in vowels:
                return self._phrase + "ay"

            if first_letter not in vowels and self._phrase[1] in vowels:
                word = self._phrase[1:] + first_letter
                return word + "ay"
            elif first_letter not in vowels and self._phrase[1] not in vowels:
                word = self._phrase[2:] + first_letter + self._phrase[1]
                return word + "ay"





