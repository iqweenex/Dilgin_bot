quiz_data = [
    {
        'question': 'Python это - ',
        'options': ['Язык программирования', 'Язык разметки', 'Змея на английском', 'Пистолет'],
        'correct_option': 0
     },
    {
        'question': 'Какой тип данных соотвествует целочисленному',
        'options': ['int', 'str', 'double', 'float'],
        'correct_option': 0
    },
    {
        'question': 'Каким способом можно преобразовать число x в число с плавающей точкой',
        'options': ['float(x)', 'double(x)', 'decimal(x)', 'int(x)'],
        'correct_option': 0
     },
    {
        'question': ' С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет. Какой режим указать в инструкции open()?',
        'options': ['x', 'w', 'r', 's'],
        'correct_option': 0
     },
    {
        'question': 'Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?',
        'options': ['T[0] = 1', 'T = (1) + T[1:]', 'T = (1,) + T[1:]', 'T.startswith(1)'],
        'correct_option': 2
    },
    {
        'question': 'Для чего в Python используется встроенная функция enumerate()?',
        'options': ['Для определения количества элементов последовательности.', 'Для одновременного итерирования по самим элементам и их индексам', 'Для сортировки элементов по значениям id.', 'Для создание множества'],
        'correct_option': 1
    },
    {
        'question': 'Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?',
        'options': ['кортеж (tuple)', 'список (list)', 'множество (set)', 'словарь (dict)'],
        'correct_option': 2
    },
    {
        'question': 'Как вывести список методов и атрибутов объекта x?',
        'options': ['help(x)', 'info(x)', '?x', 'dir(x)'],
        'correct_option': 3
    },
    
    {
        'question': ''' Как можно более кратко представить следующую запись?
            if X:
                A = Y
            else:
                A = Z''',
        'options': ['A = Y if Z else Y', 'A = Y if X else Z', 'A = X if Z else Y', 'A = X if Y else Z'],
        'correct_option': 1
    },

    {
        'question': 'Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?',
        'options': ['a = list(i for i in range(n))', 'a = [i for i in range(n)]', 'a = (i for i in range(n))', 'a = {i for i in range(n)}'],
        'correct_option': 2
    }
  ]