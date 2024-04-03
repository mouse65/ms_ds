input_string = input('Введите последовательность чисел: ')
# ваш код здесь
def find_median(inp_lst_numb):
    global med
    l_1=len(inp_lst_numb)
    if l_1%2==0:
       i=int(l_1/2)
       med=(inp_lst_numb[i-1]+inp_lst_numb[i])/2
    else:
       i=int(l_1//2)
       med=inp_lst_numb[i]
    return med
inp_lst=input_string.split(',')
# ----- удаление пробелов из строк ------------------
inp_lst_1=inp_lst.copy() # создаем служебную копию списка inp_lst
inp_lst_2=[] # объявление результирующего  входного списка с числами в виде строк
marker=False # маркед для обхода в случае некорректного ввода.
for i,val in enumerate(inp_lst):
      temp_1 = inp_lst_1[i].replace(' ', '') # замена в строке inp_lst_1[i] пробел на ''
      inp_lst_2.append(temp_1) # новый входной список чисел в виде строк с точкой
#--------------------------------------------------------------------------------------
for num in inp_lst_2:
    if num[0]!='-': # пропускаем отрицательные числа
       if not num.isdigit() and not marker:  # проверяем состоят ли вводы только из цифр?
              print('Некорректный ввод ')
              marker=True
if not marker: # обход, если некорректный ввод.
     inp_lst_numb = [int(x) for x in inp_lst_2]
     inp_lst_numb.sort()
#     print(inp_lst_numb)
     find_median(inp_lst_numb)
     print('медиана =', med)
     #