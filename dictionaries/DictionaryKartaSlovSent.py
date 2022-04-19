import pandas as pd
import spacy
import numpy as np
from SentimentType import SentimentType


class DictionaryKartaSlovSent:
    def __init__(self):
        """
        Предоставляет методы для работы со словарем тональности "КартаСловСент"
        """
        self.dictionary_file_path = 'dictionaries_data\\sentiment_dictionary_karta_slov_sent.csv'
        self._dictionary = pd.read_csv(self.dictionary_file_path, sep=';')
        self.nlp = spacy.load("ru_core_news_lg")

    def get_word_tag(self, word: str) -> str:
        """
        Определяет тональность слова по тональному словарю. Если слова нет в словаре, тональность считается нейтрольной.
        :param word: целевое слово
        :return: тональность слова
        """
        word_info = self._dictionary.loc[self._dictionary['term'] == word].values
        if word_info.size > 0:
            word_tag = word_info[0, 1]
            return word_tag
        else:
            return SentimentType.NEUTRAL.value  # Если слова нет в словаре -> нейтральная тональность

    def get_words(self) -> list[str]:
        """
        Возвращает список всех слов в словаре.
        :return: список слов
        """
        return list(self._dictionary.iloc[:, 0].values)

    def is_word_exist(self, word: str) -> bool:
        """
        Возвращает True, если слово существует.
        :param word: целевое слово
        :return: True, если слово существует.
        """
        words_in_dictionary = self._dictionary['term'].tolist()
        return word in words_in_dictionary

    def add_new_word(self, word: str, word_sentiment: str):
        """
        Добавляет новое слово в тональный словарь.
        :param word: новое слово
        :param word_sentiment: тональность словаря
        """
        new_word_index = np.searchsorted(self._dictionary.term, word) - 1
        new_word_info = pd.DataFrame({'term': [word], 'tag': [word_sentiment], 'value': [None], 'pstv': [None],
                                      'ngtv': [None], 'neut': [None], 'dunno': [None],
                                      'pstvNgtvDisagreementRatio': [None]}, columns=self._dictionary.columns,
                                     index=[new_word_index])
        self._dictionary = pd.concat([self._dictionary, new_word_info]).sort_index().reset_index(drop=True)
        self._dictionary.to_csv(self.dictionary_file_path, index=False, sep=';')

    def change_word_sentiment(self, word: str, word_sentiment: str):
        """
        Изменяет тональность существующего слова.
        :param word: целевое слово
        :param word_sentiment: новая тональность слова
        :return: 
        """
        word_index = self._dictionary.index[self._dictionary['term'] == word].tolist()[0]
        self._dictionary.at[word_index, 'tag'] = word_sentiment
        self._dictionary.to_csv(self.dictionary_file_path, index=False, sep=';')
        # TODO: Что делать со значениями кроме слова и его тега??
