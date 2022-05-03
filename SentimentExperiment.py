from SentenceDependencyTree import SentenceDependencyTree
from win32com.client import Dispatch
from SentimentType import SentimentType


def convert_sentiment_tag(tag):
    """
    Преобразует метку тональности из файла с предложениями в метку, принятую для использования в приложении
    :param tag: тональная метка из файла
    :return: тональная метка принятая для использования в приложении
    """
    if tag == 'positive':
        return SentimentType.POSITIVE.value
    elif tag == 'negative':
        return SentimentType.NEGATIVE.value
    else:
        return SentimentType.NEUTRAL.value


class SentimentExperiment:
    def __init__(self, dictionary, sentence_markup_file, progress_bar):
        self.dictionary = dictionary
        self.sentence_markup_file = sentence_markup_file
        self.progress_bar = progress_bar
        self.unknown_words = []

    def make_experiment(self) -> None:
        """
        Проходит по каждой паре "предложение-тональность" во входном файле, производит разметку,
        в соответствии с правилами, описанными в классе SentenceDependencyTree, сравнивает
        полученным результат с соответствующей разметкой в файле.
        """
        dependency_tree = SentenceDependencyTree(self.dictionary)
        count = 0
        false_positive = []
        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(
            r'D:\\Projects\\PycharmProjects\\SentimentTextMarkup\\templates\\Шаблон_эксперимент_статистика.xltx')
        ws = wb.Worksheets("Лист1")
        # ws.Range("C5").Value += 1

        print(self.sentence_markup_file.info())
        for index, row in self.sentence_markup_file.iterrows():
            sentence = row['Sentence'].replace('"', ' ')  # Предобработка
            dependency_tree.generate_tree(sentence)
            self.unknown_words.extend(dependency_tree.unknown_words)
            count += 1
            if count % 500 == 0:
                print(count)
            if convert_sentiment_tag(row['Sentiment']) == SentimentType.POSITIVE.value:
                # Таблицы контингентности
                if dependency_tree.sentence_sentiment == SentimentType.POSITIVE.value:
                    ws.Range("C5").Value += 1
                    ws.Range("D11").Value += 1
                    ws.Range("D16").Value += 1
                    ws.Range("B28").Value += 1  # Вторая таблица качества класификации

                elif dependency_tree.sentence_sentiment == SentimentType.NEGATIVE.value:
                    ws.Range("C6").Value += 1
                    ws.Range("D10").Value += 1
                    ws.Range("D16").Value += 1
                    ws.Range("C28").Value += 1  # Вторая таблица качества класификации

                elif dependency_tree.sentence_sentiment == SentimentType.NEUTRAL.value:
                    ws.Range("C6").Value += 1
                    ws.Range("D11").Value += 1
                    ws.Range("D15").Value += 1
                    ws.Range("D28").Value += 1  # Вторая таблица качества класификации
                else:
                    print(row)

            if convert_sentiment_tag(row['Sentiment']) == SentimentType.NEGATIVE.value:
                if dependency_tree.sentence_sentiment == SentimentType.POSITIVE.value:
                    ws.Range("D5").Value += 1
                    ws.Range("C11").Value += 1
                    ws.Range("D16").Value += 1
                    ws.Range("B29").Value += 1  # Вторая таблица качества класификации
                    # false_positive.append('\"'+sentence+'\"'+f", {row['Sentiment']}")

                elif dependency_tree.sentence_sentiment == SentimentType.NEGATIVE.value:
                    ws.Range("D6").Value += 1
                    ws.Range("C10").Value += 1
                    ws.Range("D16").Value += 1
                    ws.Range("C29").Value += 1  # Вторая таблица качества класификации

                elif dependency_tree.sentence_sentiment == SentimentType.NEUTRAL.value:
                    ws.Range("D6").Value += 1
                    ws.Range("C11").Value += 1
                    ws.Range("D15").Value += 1
                    ws.Range("D29").Value += 1  # Вторая таблица качества класификации
                else:
                    print(row)

            if convert_sentiment_tag(row['Sentiment']) == SentimentType.NEUTRAL.value:
                if dependency_tree.sentence_sentiment == SentimentType.POSITIVE.value:
                    ws.Range("D5").Value += 1
                    ws.Range("D11").Value += 1
                    ws.Range("C16").Value += 1
                    ws.Range("B30").Value += 1  # Вторая таблица качества класификации
                    false_positive.append('\"' + sentence + '\"' + f", {row['Sentiment']}")

                elif dependency_tree.sentence_sentiment == SentimentType.NEGATIVE.value:
                    ws.Range("D6").Value += 1
                    ws.Range("D10").Value += 1
                    ws.Range("C16").Value += 1
                    ws.Range("C30").Value += 1  # Вторая таблица качества класификации

                elif dependency_tree.sentence_sentiment == SentimentType.NEUTRAL.value:
                    ws.Range("D6").Value += 1
                    ws.Range("D11").Value += 1
                    ws.Range("C15").Value += 1
                    ws.Range("D30").Value += 1  # Вторая таблица качества класификации
                else:
                    print(row)

            self.progress_bar.setValue(self.progress_bar.value() + 1)
        self.progress_bar.setVisible(False)

        # Качество классификации. Первая таблица
        # PSTV
        ws.Range("B21").Value = ws.Range("C5").Value / (ws.Range("C5").Value + ws.Range("D5").Value)
        ws.Range("C21").Value = ws.Range("C5").Value / (ws.Range("C5").Value + ws.Range("C6").Value)
        ws.Range("D21").Value = 2 * (ws.Range("B21").Value * ws.Range("C21").Value) / (
                ws.Range("B21").Value + ws.Range("C21").Value)
        ws.Range("E21").Value = ws.Range("C5").Value + ws.Range("C6").Value

        # NGTV
        ws.Range("B22").Value = ws.Range("C10").Value / (ws.Range("C10").Value + ws.Range("D10").Value)
        ws.Range("C22").Value = ws.Range("C10").Value / (ws.Range("C10").Value + ws.Range("C11").Value)
        ws.Range("D22").Value = 2 * (ws.Range("B22").Value * ws.Range("C22").Value) / (
                ws.Range("B22").Value + ws.Range("C22").Value)
        ws.Range("E22").Value = ws.Range("C10").Value + ws.Range("C11").Value

        # NEUT
        ws.Range("B23").Value = ws.Range("C15").Value / (ws.Range("C15").Value + ws.Range("D15").Value)
        ws.Range("C23").Value = ws.Range("C15").Value / (ws.Range("C15").Value + ws.Range("C16").Value)
        ws.Range("D23").Value = 2 * (ws.Range("B23").Value * ws.Range("C23").Value) / (
                ws.Range("B23").Value + ws.Range("C23").Value)
        ws.Range("E23").Value = ws.Range("C15").Value + ws.Range("C16").Value

        # Average
        ws.Range("B24").Value = (ws.Range("B21").Value + ws.Range("B22").Value + ws.Range("B23").Value) / 3
        ws.Range("C24").Value = (ws.Range("C21").Value + ws.Range("C22").Value + ws.Range("C23").Value) / 3
        ws.Range("D24").Value = (ws.Range("D21").Value + ws.Range("D22").Value + ws.Range("D23").Value) / 3

        ws.Range("E24").Value = ws.Range("E21").Value + ws.Range("E22").Value + ws.Range("E23").Value
        ws.Range("E25").Value = ws.Range("E24").Value

        # Качество классификации. Вторая таблица
        ws.Range("E28").Value = ws.Range("B28").Value + ws.Range("C28").Value + ws.Range("D28").Value  # PSTV Всего
        ws.Range("E29").Value = ws.Range("B29").Value + ws.Range("C29").Value + ws.Range("D29").Value  # NGTV Всего
        ws.Range("E30").Value = ws.Range("B30").Value + ws.Range("C30").Value + ws.Range("D30").Value  # NEUT Всего

        self.save_unknown_words()

        # with open('false_neutral.txt', 'w', encoding='utf-8') as file:
        #     for row in false_positive:
        #         file.write(row+'\n')

    def save_unknown_words(self) -> None:
        """
        Сохраняет все неизвестные слова в файл.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique
        with open('unknown_words.txt', 'w', encoding='utf-8') as file:
            for word in self.unknown_words:
                file.write(word+'\n')
