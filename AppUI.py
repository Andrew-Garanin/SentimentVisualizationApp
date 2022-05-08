from ui.mainMDIForm import mainMDIForm
from PySide2 import QtWidgets

from sub_forms.AddNewWordForm import AddNewWordForm
from sub_forms.SentimentTextMarkupForm import SentimentTextMarkupForm
from sub_forms.ChangeWordSentimentForm import ChangeWordSentimentForm
from sub_forms.SingleSentenceSentimentTreeForm import SingleSentenceSentimentTreeForm
from dictionaries.DictionaryKartaSlovSent import DictionaryKartaSlovSent
from sub_forms.SentimentExperimentForm import SentimentExperimentForm


class SentimentVisualizationApp(mainMDIForm.Ui_mainMDIForm, QtWidgets.QMainWindow):
    def __init__(self):
        """
        Главное окно приложения.
        """
        super(SentimentVisualizationApp, self).__init__()
        self.setupUi(self)
        self.dictionary = DictionaryKartaSlovSent()
        self.mdi = self.mdiArea

        # -----------------------------Объявление дочерних форм-----------------------------
        self.sentiment_text_markup_form = None
        self.add_new_word_form = None
        self.change_word_sentiment_form = None
        self.single_sentence_sentiment_tree_form = None
        self.sentiment_experiment_form = None

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.menuSentimentTextMarkup.triggered.connect(self.menu_sentiment_text_markup)
        self.menuAddNewWord.triggered.connect(self.menu_add_new_word)
        self.menuChangeWordSentiment.triggered.connect(self.menu_change_word_sentiment)
        self.menuSingleSentence.triggered.connect(self.menu_single_sentence_sentiment_tree)
        self.menuSentimentExperiment.triggered.connect(self.menu_sentiment_experiment)
        self.menuWindowsCascade.triggered.connect(self.menu_windows_cascade)
        self.menuWindowsTiled.triggered.connect(self.menu_windows_tile)

    # -----------------------------Методы меню-----------------------------
    def menu_sentiment_text_markup(self):
        if not self.sentiment_text_markup_form:
            self.sentiment_text_markup_form = SentimentTextMarkupForm(self.dictionary)
            self.mdi.addSubWindow(self.sentiment_text_markup_form)
            self.sentiment_text_markup_form.show()
        self.sentiment_text_markup_form.setFocus()

    def menu_add_new_word(self):
        if not self.add_new_word_form:
            self.add_new_word_form = AddNewWordForm(self.dictionary)
            self.add_new_word_form.labelError.clear()
            self.add_new_word_form.newWordEdit.clear()
            self.add_new_word_form.newWordEdit.setFocus()
            self.add_new_word_form.radioButtonPSTV.setChecked(True)
            self.mdi.addSubWindow(self.add_new_word_form)
            self.add_new_word_form.show()
        self.add_new_word_form.setFocus()

    def menu_change_word_sentiment(self):
        if not self.change_word_sentiment_form:
            self.change_word_sentiment_form = ChangeWordSentimentForm(self.dictionary)
            self.change_word_sentiment_form.labelError.clear()
            self.change_word_sentiment_form.wordEdit.clear()
            self.change_word_sentiment_form.wordEdit.setFocus()
            self.change_word_sentiment_form.radioButtonPSTV.setChecked(True)
            self.mdi.addSubWindow(self.change_word_sentiment_form)
            self.change_word_sentiment_form.show()
        self.change_word_sentiment_form.setFocus()

    def menu_single_sentence_sentiment_tree(self):
        if not self.single_sentence_sentiment_tree_form:
            self.single_sentence_sentiment_tree_form = SingleSentenceSentimentTreeForm(self.dictionary)
            self.mdi.addSubWindow(self.single_sentence_sentiment_tree_form)
            self.single_sentence_sentiment_tree_form.show()
        self.single_sentence_sentiment_tree_form.setFocus()

    def menu_sentiment_experiment(self):
        if not self.sentiment_experiment_form:
            self.sentiment_experiment_form = SentimentExperimentForm(self.dictionary)
            self.mdi.addSubWindow(self.sentiment_experiment_form)
            self.sentiment_experiment_form.show()
        self.sentiment_experiment_form.setFocus()

    def menu_windows_cascade(self):
        self.mdi.cascadeSubWindows()  # Arranges subwindows in MDiArea in a cascaded fashion

    def menu_windows_tile(self):
        self.mdi.tileSubWindows()  # Arranges subwindows in MDiArea in a tiled fashion


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = SentimentVisualizationApp()
    qt_app.show()
    app.exec_()
