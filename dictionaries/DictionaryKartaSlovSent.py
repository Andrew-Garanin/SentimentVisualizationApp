import pandas as pd
import spacy
import numpy as np
from SentimentType import SentimentType
import autoit
import pymorphy2


class DictionaryKartaSlovSent:
    def __init__(self):
        """
        Предоставляет методы для работы со словарем тональности "КартаСловСент"
        """
        self.dictionary_file_path = 'dictionaries_data\\sentiment_dictionary_karta_slov_sent.csv'
        self._dictionary = pd.read_csv(self.dictionary_file_path, sep=';')
        self._morph = pymorphy2.MorphAnalyzer()
        self.nlp = spacy.load("ru_core_news_lg")
        self.unknown_words = []

    def clear_unknown_words(self) -> None:
        """
        Очищает список неизвестных слов.
        """
        self.unknown_words = []

    def show_unknown_words(self) -> None:
        """
        Открывает блокнот и записывает в него неизвестные слова конкретного предложения.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique

        autoit.run("notepad.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        for element in self.unknown_words:
            autoit.control_send("[CLASS:Notepad]", "Edit1", element + "\n")

    def save_unknown_words(self) -> None:
        """
        Сохраняет все неизвестные слова в файл.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique
        with open('unknown_words.txt', 'w', encoding='utf-8') as file:
            for word in self.unknown_words:
                file.write(word+'\n')

    def get_word_tag(self, word) -> str:
        """
        Определяет тональность слова по тональному словарю. Если слова нет в словаре, тональность считается нейтрольной.
        :param word: целевое слово
        :return: тональность слова
        """
        if word.pos_ == 'PROPN':
            return SentimentType.NEUTRAL.value  # Если слово имя собственное -> нейтральная тональность
        if word.pos_ == 'NUM':
            return SentimentType.NEUTRAL.value  # Если слово является количественным числительным -> нейтральная тональность

        lemma = self._morph.parse(word.lemma_)[0].normal_form

        word_info = self._dictionary.loc[self._dictionary['term'] == lemma].values
        if word_info.size > 0:
            word_tag = word_info[0, 1]
            return word_tag
        else:
            self.unknown_words.append(word.lemma_)
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
