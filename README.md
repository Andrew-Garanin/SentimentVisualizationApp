# SentimentVisualizationApp
____
Desktop приложение, реализующее алгоритм определения тональности, основанный на лексических
правилах для трёх классов тональности: **положительная**, **отрицательная** и **нейтральная**. 
Визуализирует работу алгоритма в виде дерева синтаксических связей предложения с раскраской узлов по тональности. 
Позволяет проводить эксперимент по выявлению и оценке качества классификации алгоритма.
Приложение включает в себя использование сторонних зависимостей, 
они перечислены в файле **requirements.txt**.

## Оглавление
____
1. [Словарь тональности](#%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C-%D1%82%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8)
2. [Правила выведения тональности](#%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B2%D1%8B%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D1%82%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8)
3. [Корпус предложений](#%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9)
4. [Шаблон для проведения эксперимента](#%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%B4%D0%BB%D1%8F-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0)
5. [Graphviz](#graphviz)
6. [Возможности приложения](#%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
7. [Структурная единица предложения](#%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B0%D1%8F-%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
    
## Словарь тональности
____
Для первоначальной разметки одиночных слов в предложениях используется находящийся в открытом доступе словарь 
тональности [КартаСловСент](https://github.com/dkulagin/kartaslov/tree/master/dataset/kartaslovsent). 
Словарь покрывает более 46 тысяч слов русского языка. Тональный словарь оформлен в виде 
файла формата **.csv** и может использоваться в составе автоматических систем анализа тональности. 
Данный словарь распространяется по лицензии [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ru).

## Правила выведения тональности
____
В качестве правил выведения тональности были взяты правила, представленные в 
[этой](https://ieeexplore.ieee.org/abstract/document/9599992/figures#figures) работе.
Каждое правило описывает получение общей тональности для пары языковых единиц. Всего таких пар пять: 
- подлежащее – сказуемое; 
- определяемое – определение; 
- дополняемый предмет – дополнение; 
- дополняемое действие – дополнение; 
- действие – обстоятельство.

Программная реализация всех правил представлена в модуле ```SentenceDependencyTree``` (метод ```calculate_sentiment_by_rules```).

## Корпус предложений
____
Для проведения экспериментов для расчёта статистических данных по точности классификации создаваемого инструмента 
был использован набор данных [OpenSentimentCorpus](https://github.com/yarfruct/open-sentiment-corpus).
Набор представляет собой несколько корпусов русских предложений, размеченных по тональности.
В таблице приведена сводная информация по числу предложений для каждого класса тональности используемого набора данных.

|  | by-majority | by-total-agreement |
|----------------|:---------:|----------------:|
| Положительная | 669 | 536 |
| Отрицательная | 1793 | 1510 |
| Нейтральная | 3062 | 2441 |
| Всего | 5524 | 4487 |

## Шаблон для проведения эксперимента
____
Для упрощения процесса формирования статистических данных был разработан шаблон 
типа **.xltx**. Он находится в разделе ```templates```.

## Graphviz
____
Приложение использует библиотеку [Graphviz](https://graphviz.readthedocs.io/en/stable/manual.html) для построение графических 
элемнтов (деревьев синтаксических связей). Обратите внимание, что она работает только для ⚠Python 3.7+⚠.

## Возможности приложения
____
✔ Ввод текста, с автоматической разметкой слов цветом, соответствущем тональности слова, согласно используемому словарю 
тональности. Зелёный цвет - положительная тональность, красный - отрицательная и чёрный - нейтральная.

✔ Построение дерева синтаксических связей предложения с раскрашенными по тональности узлами. Деревья раскрашиваются двумя
способами:
- в соответствии с тональным словарём;
- в соответствии с правилами выведения тональности.

✔ Проведение эксперимента с корпусом размеченных по тональности предложений (.csv файл), для определения точности 
классификации приложения.

✔ Редактирование используемого словаря тональности (добавление новых слов и редактирование тональности уже существующих слов).

## Структурная единица предложения
____
Для хранения информации о структурной единице предложения, то есть об одиночном слове, была предложена структура, 
представляемая парами «ключ:значение» и имеющая следующий формат:
- id - уникальный идентификатор токена в рамках отдельного предложения;
- parent_id - уникальный идентификатор токена-родителя в рамках отдельного предложения;
- text - строковое представление токена;
- dependency - маркер синтаксической зависимости в предложении;
- pos - маркер части речи токена;
- lemma - начальная форма токена;
- sentiment - метка тональности токена;
- children - список всех синтаксически-зависимых токенов для текущего. Список включает в себя элементы такой же
структуры. Если у токена нет синтаксически-зависимых токенов то, список при формировании просто делается пустым. 
  
Пример структурной единицы приведён ниже.
```text
"id": 1,
"parent_id": 2,
"text": "прекрасный",
"dependency": "amod",
"pos": "ADJ",
"lemma": "прекрасный",
"sentiment": "PSTV",
"children": []
```
