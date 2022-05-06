import json
import autoit
import spacy
from collections import Counter
from SentimentType import SentimentType


def calculate_non_rules_sentiment(parent_sentiment: str, child_sentiment: str) -> str:
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


def calculate_general_word_sentiment(sentiments: [str]) -> str:
    """
    Вычисляет общую тональность слова по его результирующему списку тональностей,руководствуясь правилом:
    тональность с наибольшим количеством вхождений является результирующей. Если число положительной и отрицательной
    тональностей одинаково, то общая тональность считается НЕЙТРАЛЬНОЙ.
    :param sentiments: список тональностей, определенный для слова, по его зависимым словам и правилам.
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


def _create_node(parents_children: [], id: int, parent_id: int, text: str,
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
    :return: индекс слова в массиве зависимых слов родителя
    """
    parents_children.append(
        {'id': id, 'parent_id': parent_id, 'text': text, 'dependency': dependency, 'pos': pos, 'lemma': lemma,
         'sentiment': sentiment, 'children': []})
    return len(parents_children) - 1


class SentenceDependencyTree:
    def __init__(self, dictionary):
        """
        Служит для формирования деревьев зависимостей слов в предложении в формате json, а также рекурсивного выведения
        тональности всего предложения, основываясь на правилах. Каждый элемент дерева
        содержит информацию о соответствующем слове: зависимость от других слов, pos-тег,
        лемму слова и его эмоциональную окраску.
        :param dictionary: Тональный словарь
        """
        self.dictionary = dictionary
        self.all_dep = ['nsubj', 'nsubj:pass', 'obj', 'iobj', 'obl', 'obl:agent', 'nmod', 'amod', 'det',
                        'advmod']  # Все виды зависимостей, подходящих под правила

        self.subject_predicate_dep = ['nsubj', 'nsubj:pass']  # Подлежащее - сказуемое
        self.object_action_dep = ['obj', 'iobj']  # Дополнение - дополняемое действие
        self.adverbial_modifier_action_dep = ['obl', 'obl:agent', 'advmod']  # Обстоятельство - действие
        self.object_subject_dep = ['nmod']  # Дополнение - дополняемый предмет
        self.definition_defined_dep = ['amod', 'det']  # Определение - определяемое

        self.sentiment_by_dictionary = None  # Дерево зависимостей с тональностью слов, определенной по словарю
        self.sentiment_by_rules = None  # Дерево зависимостей с тональностью слов, определенной по правилам
        self.found_rules = []  # Найденные в предложении правила
        self.unknown_words = []  # Неизвестные слова
        self.nlp = spacy.load("ru_core_news_lg")

    def build_trees(self, text: str) -> None:
        """
        Создаёт два дерева: на основе тонального словаря и на основе правил.
        :param text: исходный текст предложения
        """
        self.refresh_data()
        doc = self.nlp(text)
        self.sentiment_by_dictionary = dict({'text': doc.text, 'tokens': []})

        root = None
        for sentence in doc.sents:
            root = sentence.root

        if not self.dictionary.is_word_exist(root.lemma_):
            self.unknown_words.append(root.lemma_)

        _create_node(self.sentiment_by_dictionary['tokens'], root.i, -1, root.text, root.dep_, root.pos_,
                     root.lemma_, self.dictionary.get_word_tag(root))  # Корень дерева(у корня нет родителя, поэтому -1)

        self._create_tree(root.children, self.sentiment_by_dictionary['tokens'][0]['children'])
        self.sentiment_by_rules = json.loads(json.dumps(self.sentiment_by_dictionary.copy()))  # Копия для 2-го дерева
        self._change_sentiment_in_tree(self.sentiment_by_rules['tokens'], dict({'id': -1, 'children': [root]}))

        print(json.dumps(self.sentiment_by_dictionary, ensure_ascii=False, indent=4))
        print(json.dumps(self.sentiment_by_rules, ensure_ascii=False, indent=4))

    def _create_tree(self, node_children_by_lib, parents_children: []) -> None:
        """
        Создает дерево для узла, которому принадлежат зависимые слова из node_children_by_lib.
        :param node_children_by_lib: список зависимых слов текущего слова, полученный в рез-те обработки текста при
        помощи библиотеки spaCy.
        :param parents_children: массив исходящих вершин родителя (параметр children в структуре)
        """
        for child in node_children_by_lib:
            if not [child_ for child_ in child.children]:
                if child.is_punct:
                    continue
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                _create_node(parents_children, child.i, child.head.i,
                             child.text, child.dep_, child.pos_, child.lemma_,
                             self.dictionary.get_word_tag(child))
            else:
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                i = _create_node(parents_children, child.i, child.head.i,
                                 child.text, child.dep_, child.pos_, child.lemma_,
                                 self.dictionary.get_word_tag(child))
                self._create_tree(child.children, parents_children[i]['children'])

    def _change_sentiment_in_tree(self, parents_children: list[dict], parent):
        """
        Изменяет тональность слов в дереве зависимостей, путём рекурсивного прохождения дерева от листьев до корня.
        :param parents_children: список зависимых токенов элемента parent
        :param parent: токен-родитель
        :return: родитель с обновленной тональностью
        """
        dep_array = []
        for element in parents_children:
            if element['children']:
                element = self._change_sentiment_in_tree(element['children'], element)
            if element['dependency'] in self.all_dep:
                dep_array.append(self.calculate_sentiment_by_rules(parent, element))
                self.found_rules.append(
                    f"{element['text']} {parent['text']} | ПРАВИЛО: {self.get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}")
            elif (len(parent['children']) == 1) or (len(parent['children']) > 1 and element['sentiment'] != SentimentType.NEUTRAL.value) or not self.is_parent_has_rule_dep(parent):
                if element['dependency'] == 'ROOT':
                    dep_array.append(element['sentiment'])
                else:
                    dep_array.append(calculate_non_rules_sentiment(parent['sentiment'], element['sentiment']))
            elif len(parent['children']) > 1 and element['sentiment'] == SentimentType.NEUTRAL.value:
                continue

        parent['sentiment'] = calculate_general_word_sentiment(dep_array)
        return parent

    def calculate_sentiment_by_rules(self, parent, child) -> str:
        """
        Определяет тональность пары слов, синтаксическая связь которой подходит под правило.
        :param parent: родительский токен.
        :param child: токен-наследник.
        :return: тональность пары слов.
        """
        if child['dependency'] in self.subject_predicate_dep:  # Подлежащее - сказуемое
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

        if child['dependency'] in self.definition_defined_dep:  # Определение - определяемое
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

        if child['dependency'] in self.object_subject_dep:  # Дополнение - дополняемый предмет
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

        if child['dependency'] in self.object_action_dep:  # Дополнение - дополняемое действие
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

        if child['dependency'] in self.adverbial_modifier_action_dep:  # Действие - обстоятельство advmod ???
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

    def get_sentence_sentiment(self) -> str:
        """
        Возвращает общую тональность всего предложения.
        :return: тональность предложения
        """
        return self.sentiment_by_rules['tokens'][0]['sentiment']

    def is_parent_has_rule_dep(self, parent) -> bool:
        """
        Проверяет, есть ли у слова зависимое слово, подходящее под правила.
        :param parent: исследуемое слово
        :return: True, если есть у слова parent зависимое слово, подходящее под правила
        """
        for child in parent['children']:
            if child['dependency'] in self.all_dep:
                return True
        return False

    def show_unknown_words(self) -> None:
        """
        Открывает стандартное приложение "блокнот" и записывает в него неизвестные слова конкретного предложения.
        Неизвестными считаются слова, которых нет в словаре тональности.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique
        autoit.run("notepad.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        for element in self.unknown_words:
            autoit.control_send("[CLASS:Notepad]", "Edit1", element + "\n")

    def get_sentiment_type(self, dependency: str) -> str:
        """
        Определяет строковое представление правила определения тональности, на основании зависимости между парой слов.
        :param dependency: зависимость между парой слов
        :return: строковое представление правила определения тональности
        """
        if dependency in self.subject_predicate_dep:
            return 'Подлежащее - сказуемое'
        if dependency in self.object_action_dep:
            return 'Дополнение - дополняемое действие'
        if dependency in self.adverbial_modifier_action_dep:  # advmod ???
            return 'Обстоятельство - действие'
        if dependency in self.object_subject_dep:
            return 'Дополнение - дополняемый предмет'
        if dependency in self.definition_defined_dep:
            return 'Определение - определяемое'

    def refresh_data(self) -> None:
        """
        Сбрасывает информацию по предложению.
        """
        self.found_rules = []
        self.unknown_words = []
        self.sentiment_by_dictionary = None
        self.sentiment_by_rules = None
