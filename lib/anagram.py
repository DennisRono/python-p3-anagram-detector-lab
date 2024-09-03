class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            if ''.join(sorted(candidate.lower())) == self.sorted_word:
                matches.append(candidate)
        return matches
