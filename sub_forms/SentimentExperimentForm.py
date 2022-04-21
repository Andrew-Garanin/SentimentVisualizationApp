from PySide2 import QtWidgets

from SentimentType import SentimentType
from ui.sentimentExperimentForm import sentimentExperimentForm
import pandas as pd
from SentenceDependencyTree import SentenceDependencyTree
from win32com.client import Dispatch


def convert_sentiment_tag(tag):
    if tag == 'positive':
        return 'PSTV'
    elif tag == 'negative':
        return 'NGTV'
    else:
        return 'NEUT'


class SentimentExperimentForm(sentimentExperimentForm.Ui_sentimentExperimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        """
        Форма для проведения эксперимента по разметке и анализу корпуса предложений из входного файла.
        :param dictionary: Тональный словарь
        """
        super(SentimentExperimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.sentence_markup_file = None  # Путь к файлу с размеченными предложениями
        self.progress_bar = QtWidgets.QProgressBar()
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.filePathSelectButton.clicked.connect(self.menu_open)
        self.makeExperimentButton.clicked.connect(self.make_experiment)

    def menu_open(self) -> None:
        """
        Диалог выбора файла с размеченными предложениями.
        """
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.csv')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.sentence_markup_file = pd.read_csv(file, quotechar='\"', sep=',')

    def make_experiment(self) -> None:
        """
        Проходит по каждой паре "предложение-тональность" во входном файле, производит разметку,
        в соответствии с правилами, описанными в классе SentenceDependencyTree, сравнивает
        полученным результат с соответствующей разметкой в файле.
        """
        dependency_tree = SentenceDependencyTree(self.dictionary)
        count = 0
        n = 100
        self._initialize_progress_bar(n)

        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(
            r'D:\\Projects\\PycharmProjects\\SentimentTextMarkup\\templates\\Шаблон_эксперимент_статистика.xltx')
        ws = wb.Worksheets("Лист1")
        # ws.Range("C5").Value += 1
        print(self.sentence_markup_file.info())
        for index, row in self.sentence_markup_file.head(n).iterrows():
            dependency_tree.generate_tree(row['Sentence'])
            count += 1
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

            self.progress_bar.setValue(self.progress_bar.value()+1)
        self.progress_bar.setVisible(False)
        print(count)

        # Качество классификации. Первая таблица
        # PSTV
        ws.Range("B21").Value = ws.Range("C5").Value/(ws.Range("C5").Value + ws.Range("D5").Value)
        ws.Range("C21").Value = ws.Range("C5").Value/(ws.Range("C5").Value + ws.Range("C6").Value)
        ws.Range("D21").Value = 2 * (ws.Range("B21").Value * ws.Range("C21").Value)/(ws.Range("B21").Value + ws.Range("C21").Value)
        ws.Range("E21").Value = ws.Range("C5").Value + ws.Range("C6").Value

        # NGTV
        ws.Range("B22").Value = ws.Range("C10").Value/(ws.Range("C10").Value + ws.Range("D10").Value)
        ws.Range("C22").Value = ws.Range("C10").Value/(ws.Range("C10").Value + ws.Range("C11").Value)
        ws.Range("D22").Value = 2 * (ws.Range("B22").Value * ws.Range("C22").Value)/(ws.Range("B22").Value + ws.Range("C22").Value)
        ws.Range("E22").Value = ws.Range("C10").Value + ws.Range("C11").Value

        # NEUT
        ws.Range("B23").Value = ws.Range("C15").Value/(ws.Range("C15").Value + ws.Range("D15").Value)
        ws.Range("C23").Value = ws.Range("C15").Value/(ws.Range("C15").Value + ws.Range("C16").Value)
        ws.Range("D23").Value = 2 * (ws.Range("B23").Value * ws.Range("C23").Value)/(ws.Range("B23").Value + ws.Range("C23").Value)
        ws.Range("E23").Value = ws.Range("C15").Value + ws.Range("C16").Value

        # Average
        # ws.Range("B24").Value = (ws.Range("C5").Value + ws.Range("C10").Value + ws.Range("C15").Value)/(ws.Range("C5").Value + ws.Range("D5").Value +
        #                                                                                                 ws.Range("C10").Value + ws.Range("D10").Value +
        #                                                                                                 ws.Range("C15").Value + ws.Range("D15").Value)
        # ws.Range("C24").Value = (ws.Range("C5").Value + ws.Range("C10").Value + ws.Range("C15").Value)/(ws.Range("C5").Value + ws.Range("C6").Value +
        #                                                                                                 ws.Range("C10").Value + ws.Range("C11").Value +
        #                                                                                                 ws.Range("C15").Value + ws.Range("C16").Value)
        # ws.Range("D24").Value = 2 * (ws.Range("B24").Value * ws.Range("C24").Value)/(ws.Range("B24").Value + ws.Range("C24").Value)
        # ws.Range("E24").Value = ws.Range("E21").Value + ws.Range("E22").Value + ws.Range("E23").Value
        ws.Range("E24").Value = ws.Range("E21").Value + ws.Range("E22").Value + ws.Range("E23").Value
        ws.Range("E25").Value = ws.Range("E24").Value

        # Качество классификации. Вторая таблица
        ws.Range("E28").Value = ws.Range("B28").Value + ws.Range("C28").Value + ws.Range("D28").Value  # PSTV Всего
        ws.Range("E29").Value = ws.Range("B29").Value + ws.Range("C29").Value + ws.Range("D29").Value  # NGTV Всего
        ws.Range("E30").Value = ws.Range("B30").Value + ws.Range("C30").Value + ws.Range("D30").Value  # NEUT Всего

    def _initialize_progress_bar(self, maximum: int) -> None:
        """
        Устанавливает параметры для элемента формы progress bar и добавляет его на форму.
        :param maximum: число предложений во входном файле
        """
        self.progress_bar.setRange(0, maximum)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(17)
        self.progress_bar.setFixedWidth(125)

        self.statusbar.addPermanentWidget(self.progress_bar)
        self.progress_bar.setVisible(True)
