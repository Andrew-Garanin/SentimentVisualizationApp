import pandas as pd
import spacy
import numpy as np


class DictionaryKartaSlovSent:
    def __init__(self):
        self.csv_file_path = 'D:\\Projects\\PycharmProjects\\SentimentTextMarkup\\dictionaries_data\\sentiment_dictionary_karta_slov_sent.csv'
        self._map_data = pd.read_csv(self.csv_file_path, sep=';')
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

    def get_words(self):
        return self._map_data.iloc[:, 0]

    def is_word_already_exist(self, term):
        col_one_list = self._map_data['term'].tolist()
        a = term in col_one_list
        return a

    def add_new_word(self, term, word_sentiment):
        index = np.searchsorted(self._map_data.term, term)-1
        df2 = pd.DataFrame({'term': [term],
                            'tag': [word_sentiment],
                            'value': [None],
                            'pstv': [None],
                            'ngtv': [None],
                            'neut': [None],
                            'dunno': [None],
                            'pstvNgtvDisagreementRatio': [None]}, columns=self._map_data.columns, index=[index])
        self._map_data = pd.concat([self._map_data, df2]).sort_index().reset_index(drop=True)
        self._map_data.to_csv("D:\\Projects\\PycharmProjects\\SentimentTextMarkup\\dictionaries_data\\sentiment_dictionary_karta_slov_sent.csv", index=False, sep=';')

    def change_word_sentiment(self, term, wor_sentiment):
        pass