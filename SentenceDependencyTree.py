from collections import Counter
import json
from SentimentType import SentimentType
import autoit
import spacy


def get_sentiment_type(dependency: str) -> str:
    """
    Определяет строковое представление 
    :param dependency:
    :return:
    """
    if dependency in ['nsubj', 'nsubj:pass']:
        return 'Подлежащее - сказуемое'
    if dependency in ['obj', 'iobj']:
        return 'Дополнение - дополняемое действие'
    if dependency in ['obl', 'obl:agent', 'advmod']:  # advmod ???
        return 'Обстоятельство - действие'
    if dependency in ['nmod']:
        return 'Дополнение - дополняемый предмет'
    if dependency in ['amod', 'det']:
        return 'Определение - определяемое'


class SentenceDependencyTree:
    def __init__(self, dictionary):
        """
        Реализует дерево зависимостей слов в предложении в формате json. Каждый элемент дерева
        содержит информацию о соответствующем слове: зависимость от других слов, pos-тег,
        лемму слова и его эмоциональную окраску.
        :param dictionary: Тональный словарь
        """
        self.dictionary = dictionary
        self.main_dep = ['nsubj', 'nsubj:pass', 'obj', 'iobj', 'obl', 'obl:agent', 'nmod', 'amod', 'det',
                         'advmod']  # Зависимости пар слов, за которыми следим
        self.sentiment_by_dictionary = None  # Дерево зависимостей с тональностью слов, определенной по тональному словарю
        self.sentiment_by_rules = None  # Дерево зависимостей с тональностью слов, определенной по правилам
        self.found_rules = []  # Найденные в предложении правила
        self.unknown_words = []  # Неизвестные слова
        self.nlp = spacy.load("ru_core_news_lg")

    def get_sentence_sentiment(self):
        return self.sentiment_by_rules['tokens'][0]['sentiment']

    def refresh_data(self) -> None:
        """
        Сбрасывает информацию по предложению.
        """
        self.found_rules = []
        self.unknown_words = []
        self.sentiment_by_dictionary = None
        self.sentiment_by_rules = None

    def _create_node(self, parents_children: [], id: int, parent_id: int, text: str,
                     dependency: str, pos: str, lemma: str, sentiment: str) -> int:
        """
        Создаёт вершину дерева.
        :param parents_children: массив исходящих вершин родителя
        :param id: уникальный, в пределах дерева, идентификатор вершины
        :param parent_id: идентификатор родителя
        :param text: строковое представление слова
        :param dependency: зависимость слова от его родителя
        :param pos: pos-тег слова
        :param lemma: лемма слова
        :param sentiment: тональность слова
        :return: индекс слова в массиве исходящих вершин родителя
        """
        parents_children.append(
            {'id': id, 'parent_id': parent_id, 'text': text, 'dependency': dependency, 'pos': pos, 'lemma': lemma,
             'sentiment': sentiment, 'children': []})
        return len(parents_children) - 1

    def _create_tree(self, token, parents_children: []) -> None:
        """
        Рекурсивно создает дерево в корне со значением token.
        :param token: корень создаваемого дерева
        :param parents_children: массив исходящих вершин родителя
        :return:
        """
        for child in token:
            if not [child_ for child_ in child.children]:
                if child.is_punct:
                    continue
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                self._create_node(parents_children, child.i, child.head.i,
                                  child.text, child.dep_, child.pos_, child.lemma_,
                                  self.dictionary.get_word_tag(child))
            else:
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                i = self._create_node(parents_children, child.i, child.head.i,
                                      child.text, child.dep_, child.pos_, child.lemma_,
                                      self.dictionary.get_word_tag(child))
                self._create_tree(child.children, parents_children[i]['children'])

    def build_trees(self, text):
        """
        Создаёт два дерева: на основе тонального словаря и на основе правил
        :param text: исходный текст предложения
        """
        self.refresh_data()
        doc = self.nlp(text)
        self.sentiment_by_dictionary = dict()
        self.sentiment_by_dictionary['text'] = doc.text
        self.sentiment_by_dictionary['tokens'] = []

        root = None
        for sentence in doc.sents:
            root = sentence.root

        if not self.dictionary.is_word_exist(root.lemma_):
            self.unknown_words.append(root.lemma_)

        self._create_node(self.sentiment_by_dictionary['tokens'], root.i, -1, root.text, root.dep_, root.pos_,
                          root.lemma_, self.dictionary.get_word_tag(root))  # Корень дерева

        self._create_tree(root.children, self.sentiment_by_dictionary['tokens'][0]['children'])
        self.sentiment_by_rules = json.loads(json.dumps(self.sentiment_by_dictionary.copy()))  # Копия для 2-го дерева
        self.change_sentiment_in_tree(self.sentiment_by_rules['tokens'], dict({'id': -1, 'children': [root]}))  # Поиск правил

        # print(json.dumps(self.sentiment_by_dictionary, ensure_ascii=False, indent=4))
        # print(json.dumps(self.sentiment_by_rules, ensure_ascii=False, indent=4))

    def is_parent_has_main_dep(self, parent) -> bool:
        for child in parent['children']:
            if child['dependency'] in self.main_dep:
                return True
        return False

    def show_unknown_words(self) -> None:
        """
        Открывает блокнот и записывает в него неизвестные слова конкретного предложения.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique

        autoit.run("notepad.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        for element in self.unknown_words:
            autoit.control_send("[CLASS:Notepad]", "Edit1", element + "\n")

    def change_sentiment_in_tree(self, json_tree: list[dict], parent):
        dep_array = []
        for element in json_tree:
            if element['children']:
                element = self.change_sentiment_in_tree(element['children'], element)
            if element['dependency'] in self.main_dep:
                dep_array.append(self.calculate_sentiment_by_rules(parent, element))
                self.found_rules.append(
                    f"{element['text']} {parent['text']} | ПРАВИЛО: {get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}")

            elif (len(parent['children']) == 1) or (len(parent['children']) > 1 and element['sentiment'] != SentimentType.NEUTRAL.value) or not self.is_parent_has_main_dep(parent):
                if element['dependency'] == 'ROOT':
                    dep_array.append(element['sentiment'])
                else:
                    dep_array.append(self.calculate_non_rules_sentiment(parent['sentiment'], element['sentiment']))
            elif len(parent['children']) > 1 and element['sentiment'] == SentimentType.NEUTRAL.value:
                continue

        parent['sentiment'] = self.calculate_general_word_sentiment(dep_array)
        return parent

    def calculate_non_rules_sentiment(self, parent_sentiment: str, child_sentiment: str) -> str:
        """
        Определяет тональность пары слов, синтаксическая зависимость которой, не подходит ни под одно правило.
        :param parent_sentiment: тональность родительского слова.
        :param child_sentiment: тональность слова-наследника.
        :return: тональность пары слов.
        """
        if parent_sentiment == child_sentiment:
            return parent_sentiment

        if parent_sentiment == SentimentType.NEGATIVE.value and child_sentiment == SentimentType.POSITIVE.value:
            return SentimentType.NEUTRAL.value

        if child_sentiment == SentimentType.NEGATIVE.value and parent_sentiment == SentimentType.POSITIVE.value:
            return SentimentType.NEUTRAL.value

        if parent_sentiment == SentimentType.POSITIVE.value and child_sentiment == SentimentType.NEUTRAL.value:
            return SentimentType.POSITIVE.value

        if child_sentiment == SentimentType.POSITIVE.value and parent_sentiment == SentimentType.NEUTRAL.value:
            return SentimentType.POSITIVE.value

        if parent_sentiment == SentimentType.NEGATIVE.value and child_sentiment == SentimentType.NEUTRAL.value:
            return SentimentType.NEGATIVE.value

        if child_sentiment == SentimentType.NEGATIVE.value and parent_sentiment == SentimentType.NEUTRAL.value:
            return SentimentType.NEGATIVE.value

    def calculate_sentiment_by_rules(self, parent, child) -> str:
        """
        Определяет тональность пары слов, синтаксическая связь которой подходит под правило.
        :param parent: родительский токен.
        :param child: Токен-наследник.
        :return: тональность пары слов.
        """
        if child['dependency'] in ['nsubj', 'nsubj:pass']:  # Подлежащее - сказуемое
            if child['sentiment'] == SentimentType.POSITIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.POSITIVE.value
            if child['sentiment'] == SentimentType.NEGATIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEUTRAL.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEGATIVE.value
            if child['sentiment'] == SentimentType.NEUTRAL.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

        if child['dependency'] in ['amod', 'det']:  # Определение - определяемое
            if child['sentiment'] == SentimentType.NEGATIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEGATIVE.value  # было neutral
            if child['sentiment'] == SentimentType.POSITIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEUTRAL.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.POSITIVE.value
            if child['sentiment'] == SentimentType.NEUTRAL.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    if parent['dependency'] in ['nsubj', 'nsubj:pass',
                                                'ROOT']:  # Положительный, если определяется подлежащее ROOT????
                        return SentimentType.POSITIVE.value
                    elif parent['dependency'] in ['obj', 'iobj', 'nmod']:  # нейтральный, если определяется дополнение
                        return SentimentType.NEUTRAL.value
                    else:
                        return SentimentType.NEUTRAL.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

        if child['dependency'] in ['nmod']:  # Дополнение - дополняемый предмет
            if child['sentiment'] == SentimentType.NEGATIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEUTRAL.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEGATIVE.value
            if child['sentiment'] == SentimentType.POSITIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.POSITIVE.value
            if child['sentiment'] == SentimentType.NEUTRAL.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

        if child['dependency'] in ['obj', 'iobj']:  # Дополнение - дополняемое действие
            if child['sentiment'] == SentimentType.NEGATIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEGATIVE.value
            if child['sentiment'] == SentimentType.POSITIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

            if child['sentiment'] == SentimentType.NEUTRAL.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

        if child['dependency'] in ['obl', 'obl:agent', 'advmod']:  # Действие - обстоятельство advmod ???
            if child['dependency'] == 'advmod' and child['text'].lower() == 'не':
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value
            if child['sentiment'] == SentimentType.NEGATIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value
            if child['sentiment'] == SentimentType.POSITIVE.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEUTRAL.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.POSITIVE.value
            if child['sentiment'] == SentimentType.NEUTRAL.value:
                if parent['sentiment'] == SentimentType.POSITIVE.value:
                    return SentimentType.POSITIVE.value
                if parent['sentiment'] == SentimentType.NEGATIVE.value:
                    return SentimentType.NEGATIVE.value
                if parent['sentiment'] == SentimentType.NEUTRAL.value:
                    return SentimentType.NEUTRAL.value

    def calculate_general_word_sentiment(self, sentiments: [str]) -> str:
        """
        Вычисляет общую тональность слова по его результирующему списку тональностей, путем выбора одной тональности,
        руководствуясь правилом: тональность с наибольшим количкством вхождений является результирующей.
        :param sentiments: список тональностей, определнный для слова, по его наследниками и правилам.
        :return: результирующая тональность слова.
        """
        c = Counter(sentiments)
        if len(c) == 1 and SentimentType.NEUTRAL.value in c:
            return SentimentType.NEUTRAL.value
        if SentimentType.NEUTRAL.value in c:
            c.pop(SentimentType.NEUTRAL.value, None)
        max_val = max(c.values())
        final_dict = {k: v for k, v in c.items() if v == max_val}
        if len(final_dict) == 1:
            return list(final_dict.keys())[0]
        else:
            if len(final_dict) == 2:
                return SentimentType.NEUTRAL.value
            else:
                return list(final_dict.keys())[0]
