from PySide2.QtGui import *
from PySide2.QtCore import *


class Highlighter:
    def __init__(self, document, cursor, text_field, dictionary):
        self.dictionary = dictionary
        self.document = document
        self.highlightingRules = []
        self.cursor = cursor
        self.text_field = text_field

        # PSTV
        brush = QBrush(Qt.darkGreen, Qt.SolidPattern)
        pstv_rule_format = QTextCharFormat()
        pstv_rule_format.setForeground(brush)
        sentiment = 'PSTV'
        rule = HighlightingRule(sentiment, pstv_rule_format)
        self.highlightingRules.append(rule)

        # NGTV
        brush = QBrush(Qt.red, Qt.SolidPattern)
        ngtv_rule_format = QTextCharFormat()
        ngtv_rule_format.setForeground(brush)
        sentiment = 'NGTV'
        rule = HighlightingRule(sentiment, ngtv_rule_format)
        self.highlightingRules.append(rule)

    def highlight_text(self):
        text = self.document.toPlainText()
        for rule in self.highlightingRules:
            idx = 0
            text_array = self.dictionary.nlp(text)
            for word in text_array:
                lemma = word.lemma_
                tag = self.dictionary.get_word_tag(lemma)
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
        if sentiment == 'PSTV':
            rule_format = self.highlightingRules[0].rule_format
        elif sentiment == 'NGTV':
            rule_format = self.highlightingRules[1].rule_format
        else:
            rule_format = QTextCharFormat()

        self.cursor.beginEditBlock()
        self.cursor.setPosition(index, QTextCursor.MoveAnchor)
        self.cursor.setPosition(index + length, QTextCursor.KeepAnchor)
        self.cursor.setCharFormat(rule_format)
        self.cursor.endEditBlock()


class HighlightingRule:
    def __init__(self, sentiment_type, rule_format):
        self.sentiment_type = sentiment_type
        self.rule_format = rule_format
