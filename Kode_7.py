from pprint import pprint
import  string
from tokenize import endpats

class WordsFinder:
    def __init__(self, name):
        self.file_names = {}
        self.name = name
        self.dict1 = {}

    def get_all_words(self):
        all_words = []
        self.file_names[self.name] = all_words
        with open(self.name, encoding='utf8') as file:
            for line in file:
                dont_matkers = line.translate(str.maketrans('','', string.punctuation))
                dont_matkers = dont_matkers.lower()
                dont_matkers = dont_matkers.rstrip('\n')
                all_words = all_words + dont_matkers.split(' ')
                self.file_names[self.name] = all_words
        return self.file_names

    def find(self, word):
        i = 0
        for self.name, words in self.file_names.items():
            w = word.lower()
            for k in words:
                i += 1
                if k == w:
                    self.dict1[self.name] = i
                    break
        return self.dict1

    def count(self, word):
        i = 0
        for self.name, words in self.file_names.items():
            w = word.lower()
            for k in words:
                if k == w:
                    i += 1
            self.dict1[self.name] = i
        return self.dict1

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
