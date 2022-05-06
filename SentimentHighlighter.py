from PySide2.QtGui import *
from PySide2.QtCore import *
import spacy
from SentimentType import SentimentType
from bs4 import BeautifulSoup


class SentimentHighlighter:
    def __init__(self, document, cursor, text_field, dictionary):
        self.dictionary = dictionary
        self.document = document
        self.highlightingRules = []
        self.cursor = cursor
        self.text_field = text_field
        self.nlp = spacy.load("ru_core_news_lg")

        # PSTV
        brush = QBrush(Qt.darkGreen, Qt.SolidPattern)
        pstv_rule_format = QTextCharFormat()
        pstv_rule_format.setForeground(brush)
        sentiment = SentimentType.POSITIVE.value
        rule = HighlightingRule(sentiment, pstv_rule_format)
        self.highlightingRules.append(rule)

        # NGTV
        brush = QBrush(Qt.red, Qt.SolidPattern)
        ngtv_rule_format = QTextCharFormat()
        ngtv_rule_format.setForeground(brush)
        sentiment = SentimentType.NEGATIVE.value
        rule = HighlightingRule(sentiment, ngtv_rule_format)
        self.highlightingRules.append(rule)

    def highlight_text(self):
        text = self.document.toPlainText()
        for rule in self.highlightingRules:
            idx = 0
            text_array = self.nlp(text)
            for word in text_array:
                tag = self.dictionary.get_word_tag(word)
                if tag == rule.sentiment_type:
                    length = len(word)

                    self.cursor.beginEditBlock()
                    self.cursor.setPosition(idx, QTextCursor.MoveAnchor)
                    self.cursor.setPosition(idx + length, QTextCursor.KeepAnchor)
                    self.cursor.setCharFormat(rule.rule_format)
                    self.cursor.endEditBlock()

                    idx = idx + len(word)
                    if len(text) > idx and text[idx] == ' ':
                        idx += 1
                else:
                    idx = idx + len(word)
                    if len(text) > idx and text[idx] == ' ':
                        idx += 1

    def highlight_single_word(self, index, length, sentiment):
        if sentiment == SentimentType.POSITIVE.value:
            rule_format = self.highlightingRules[0].rule_format
        elif sentiment == SentimentType.NEGATIVE.value:
            rule_format = self.highlightingRules[1].rule_format
        else:
            rule_format = QTextCharFormat()  # нейтральная

        self.cursor.beginEditBlock()
        self.cursor.setPosition(index, QTextCursor.MoveAnchor)
        self.cursor.setPosition(index + length, QTextCursor.KeepAnchor)
        self.cursor.setCharFormat(rule_format)
        self.cursor.endEditBlock()

    def save_text_to_html(self):
        cursor = QTextCursor(self.document)
        html = cursor.document().toHtml()
        soup = BeautifulSoup(html, features="html.parser")
        soup.find('meta')['charset'] = 'utf-8'
        with open('texts_data\\test.html', 'w', encoding='UTF-8') as f:
            f.write(str(soup))


class HighlightingRule:
    def __init__(self, sentiment_type, rule_format):
        self.sentiment_type = sentiment_type
        self.rule_format = rule_format
