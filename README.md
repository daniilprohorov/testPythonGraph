# testPythonGraph
Тестовое задание выполненное на python3

## Поиск всех путей в дереве

Реализация допустима на любом языке программирования, но предпочтительней
использовать Python или Scala.

Дан файл, содержащий строки вида:

A->B;

B->C;

A->C;

A->D;

D->E;

E->F;

D->G;

G->H;

G->I;


В них закодировано дерево, будем считать что все имена вершин могут
состоять только из одного символа A-Z, первая вершина первой строки
всегда корень.

Необходимо вывести на стандартный вывод все пути от корня до листьев.
Порядок вывода строк не важен.

Вывод для примера выше:

ABC

AC

ADEF

ADGH

ADGI


Вместе с кодом нужно описать способ запуска. Не лишним будет описать
слабые места алгоритма и границы применимости. Тесты приветствуются.

Пример дерева доступен в виде описания для graphviz в файле tree-task.dot


## Плюсы и минусы моего решения:
Минусы алгоритма наверное в том, что я использую словарь для хранения графа, думаю это не самый быстрый способ доступа к элементам, но во многом удобный. Также думал, что будет не правильно работать с циклами(в графе), но проверил, с циклами также нормально работает. Также думал как достать информацию о графе, почитал про всякие библиотеки pydot, graphviz, частично разобрался, но решил, что если я сделаю с ними, то это будет 10 строчек кода, а это бессмысленно, потому что вам нужно посмотреть как все-таки я программирую, алгоритмы. и все такое прочее, как я понимаю, поэтому читаю файл построчно, убираю все лишнее, и уже из него строю граф в словаре. Ничего сложного сначала не было, но потом все-таки, выводить пути, оказалась не самой простой задачей, особенно при моем хранении в словаре, когда я храню ключ, и список смежных узлов, но все работает, хотя и пришлось напрячь голову и порисовать на листочке.
