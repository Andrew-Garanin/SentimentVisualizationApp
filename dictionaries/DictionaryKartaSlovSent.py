import pandas as pd
import spacy


class DictionaryKartaSlovSent:
    def __init__(self):
        self._map_data = pd.read_csv('../dictionaries_data/sentiment_dictionary_karta_slov_sent.csv', sep=';')
        self.nlp = spacy.load("ru_core_news_md")

    def get_word_tag(self, term):
        a = self._map_data.loc[self._map_data['term'] == term]
        b = a.values
        if b.size > 0:
            print(b[0, 0], b[0, 1])
            return b[0, 1]
        else:
            print(f"{term} - нет в словаре.")
            return '-'
