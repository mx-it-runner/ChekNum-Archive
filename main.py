import pandas as pd
import sys
import os

# Чтение данных из файлов DEF-9xx.xlsx и numbers.xlsx
def_data = pd.read_excel('Data.xlsx')
numbers_data = pd.read_excel('numbers.xlsx')

# Создание пустого списка для хранения сопоставленных данных
mapped_data = []
error_data = []

non_number = 0
complit_number = 0
# empty_string = 0

# Итерация по каждому номеру из файла numbers.xlsx
for number in numbers_data['Numbers']:
    # Получение кода оператора (АБС) и номера для диапазона
    x = str(number)
    
    if (len(x) == 11):

        kod_operatora = x[1:4]
        nomer = x[4:11]

        # Поиск соответствующего диапазона значений "От" и "До"
        match = def_data[(def_data['АВС/ DEF'] == int(kod_operatora)) & (def_data['От'] <= int(nomer)) & (def_data['До'] >= int(nomer))]    
    
        # Проверка, найдено ли совпадение
        if not match.empty:
            # Получение значений оператора и региона для найденного диапазона
            complit_number += 1

            operator = match['Оператор'].iloc[0]
            region = match['Регион'].iloc[0]
        
            # Добавление сопоставленных данных в список
            mapped_data.append([number, operator, region])
        else:
            non_number += 1
            error_data.append([number])
    
    else:
        non_number += 1
        error_data.append([number])

print("Установленных номеров:", complit_number)
print("Неустановленных номеров:", non_number)
# print("Пустых строк:", empty_string)


if os.path.exists('output.xlsx'):
    os.remove('output.xlsx')

if os.path.exists('ErrorNum.xlsx'):
    os.remove('ErrorNum.xlsx')

# Создание DataFrame для сопоставленных данных
mapped_df = pd.DataFrame(mapped_data, columns=['Номер', 'Оператор сотовой связи', 'Регион'])
error_data_df = pd.DataFrame(error_data, columns=['Номер'])

# Сохранение DataFrame в новый файл output.xlsxto_excel
mapped_df.to_excel('output.xlsx', index=False)
error_data_df.to_excel('ErrorNum.xlsx', index=False)
