class WordsFinder:
    def  __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
              words = [word.strip(',.=!?;:-').lower() for word in file.read().split()]
              all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            try:
                index = words.index(word.lower())
                result[file_name] = index + 1
            except ValueError:
                pass
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
