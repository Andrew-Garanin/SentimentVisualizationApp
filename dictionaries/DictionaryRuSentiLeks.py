import pandas as pd
import spacy
import csv


class DictionaryRuSentiLeks:
    def __init__(self):
        self._map_data = self._read_dictionary_csv()
        self.nlp = spacy.load("ru_core_news_md")

    def _read_dictionary_csv(self):
        with open('../dictionaries_data/sentiment_dictionary_ru_senti_leks.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            row1 = next(reader)

            list1 = []
            for index, row in enumerate(reader):
                if len(row) > 6:
                    row.append('')
                list1.append(row)
        return pd.DataFrame(list1, columns=row1, index=None)

    def get_word_tag(self, term):
        a = self._map_data.loc[self._map_data['term'] == term]
        b = a.values
        if b.size > 0:
            print(b[0, 0], b[0, 3])
            if b[0, 3] == 'positive':
                return 'PSTV'
            if b[0, 3] == 'negative':
                return 'NGTV'
            if b[0, 3] == 'neutral':
                return 'NEUT'
            if b[0, 3] == 'positive/negative':
                return 'CTXDEP'  # Зависит от контекста
        else:
            print(f"{term} - нет в словаре.")
            return '-'
