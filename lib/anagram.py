# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        other_word_lower = other_word.lower()

        # Words of different lengths can't be anagrams
        if len(self.word) != len(other_word_lower):
            return False

        # Anagrams have the same sorted letters
        return sorted(self.word) == sorted(other_word_lower)
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']
