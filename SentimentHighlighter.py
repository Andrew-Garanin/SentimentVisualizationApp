"""
Python Syntax Highlighting Example

Copyright (C) 2009 Carson J. Q. Farmer

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public Licence as published by the Free Software
Foundation; either version 2 of the Licence, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public Licence for more
details.

You should have received a copy of the GNU General Public Licence along with
this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA  02110-1301, USA
"""

from PySide2.QtGui import *
from PySide2.QtCore import *
from dictionaries.DictionaryKartaSlovSent import DictionaryKartaSlovSent
from dictionaries.DictionaryRuSentiLeks import DictionaryRuSentiLeks


class SentimentHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        QSyntaxHighlighter.__init__(self, parent)
        self.parent = parent
        self.highlightingRules = []
        self.dictionary = DictionaryKartaSlovSent()
        #self.dictionary = DictionaryRuSentiLeks()

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

    def highlightBlock(self, text):
        for rule in self.highlightingRules:
            # expression = QRegExp(rule.pattern)
            # index = expression.indexIn(text)

            idx = 0
            text_array = self.dictionary.nlp(text)
            for word in text_array:
                lemma = word.lemma_
                tag = self.dictionary.get_word_tag(lemma)
                if tag == rule.sentiment_type:
                    length = len(word)
                    self.setFormat(idx, length, rule.rule_format)
                    idx = idx + len(word)
                    if len(text) > idx and text[idx] == ' ':
                        idx += 1
                else:
                    idx = idx + len(word)
                    if len(text) > idx and text[idx] == ' ':
                        idx += 1

            # while index >= 0:
            #     length = expression.matchedLength()
            #     self.setFormat(index, length, rule.format)
            #     index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)


class HighlightingRule:
    def __init__(self, sentiment_type, rule_format):
        self.sentiment_type = sentiment_type
        self.rule_format = rule_format
