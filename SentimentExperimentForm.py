from PySide2 import QtWidgets
from ui.sentimentExperimentForm import sentimentExperimentForm
import pandas as pd
from SentenceDependencyTree import SentenceDependencyTree


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
        for index, row in self.sentence_markup_file.head(n).iterrows():
            dependency_tree.generate_tree(row['Sentence'])

            if convert_sentiment_tag(row['Sentiment']) == dependency_tree.sentence_sentiment:
                count += 1
            self.progress_bar.setValue(self.progress_bar.value()+1)
        print(count)
        self.progress_bar.setVisible(False)

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
