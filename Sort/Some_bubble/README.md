<h2>Пузырьковая сортировка и её улучшения</h2>

<h3>Сортировка пузырьком </h3>

Сортировка пузырьком — один из самых известных алгоритмов сортировки. 
Здесь нужно последовательно сравнивать значения соседних элементов и менять числа местами,
если предыдущее оказывается больше последующего. Таким образом элементы с большими значениями 
оказываются в конце списка, а с меньшими остаются в начале.


<h3>Сортировка перемешиванием (шейкерная сортировка) </h3>


Шейкерная сортировка отличается от пузырьковой тем, 
что она двунаправленная: алгоритм перемещается не строго слева направо, 
а сначала слева направо, затем справа налево.


<h3>Сортировка расчёской </h3>

Сортировка расчёской — улучшение сортировки пузырьком. 
Её идея состоит в том, чтобы «устранить» элементы с небольшими значения в 
конце массива, которые замедляют работу алгоритма. Если при пузырьковой и шейкерной
сортировках при переборе массива сравниваются соседние элементы, то при «расчёсывании»
сначала берётся достаточно большое расстояние между сравниваемыми значениями, а потом оно 
сужается вплоть до минимального.

Первоначальный разрыв нужно выбирать не случайным образом, а с учётом специальной величины 
— фактора уменьшения, оптимальное значение которого равно 1,247. Сначала расстояние 
между элементами будет равняться размеру массива, поделённому на 1,247; на каждом 
последующем шаге расстояние будет снова делиться на фактор уменьшения — и так до окончания 
работы алгоритма.


