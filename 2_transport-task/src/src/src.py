from TASK1 import *
from TASK2_1 import *
from TASK2_2 import *

from utils import *
from potencial_method import *

# работаем с введенными из TASK.py переменными:
#                 M, N, m_count, n_count, coefs

# TASK1: РЕШИТЬ ЗАДАЧУ МЕТОДОМ ПОТЕНЦИАЛОВ С НАЧАЛЬНЫМ ПРИБЛИЖЕНИЕМ МЕТОДОМ ПОТЕНЦИАЛОВ
#        (с автоматическим проверкой на закрытость задачи)
#
# +
#
# TASK3: ОПИСАТЬ АЛГОРИТМ ПОИСКА ЦИКЛА ПЕРЕСЧЕТА И ВЫВЕСТИ ВСЕ ЦИКЛЫ ПЕРЕСЧЕТА
M, N, m_count, n_count, coefs = make_task_close(M, N, m_count, n_count, coefs)
poten_sol = potencial_solution(M, N, m_count, n_count, coefs, True)
print_result(poten_sol, coefs)

# TASK2: ПРИДУМАТЬ СОБСТВЕННЫЙ ПРИМЕР И ПОКАЗАТЬ, КАК АВТОМАТИЧЕСКИ ПРИВОДИТСЯ ЗАДАЧА
#        К ЗАКРЫТОМУ ВИДУ
print("\n")
M21, N21, m_count21, n_count21, coefs21 = make_task_close(M21, N21, m_count21, n_count21, coefs21)
poten_sol = potencial_solution(M21, N21, m_count21, n_count21, coefs21, False)
print_result(poten_sol, coefs21)

print("\n")
M22, N22, m_count22, n_count22, coefs22 = make_task_close(M22, N22, m_count22, n_count22, coefs22)
poten_sol = potencial_solution(M22, N22, m_count22, n_count22, coefs22, False)
print_result(poten_sol, coefs22)


# TASK4: РЕШИТЬ ТУ ЖЕ ЗАДАЧУ МЕТОДОМ ПЕРЕБОРА КРАЙНИХ ТОЧЕК
M, N, m_count, n_count, coefs = make_task_close(M, N, m_count, n_count, coefs)
min_task, A_matr, b_vec = to_canon(M, N, m_count, n_count, coefs)
# тут уже кодик с канон задачей и переборе как а-ля 1 лаба
