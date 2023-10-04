import sys
import pandas as pd
import numpy as np

# Чтение данных из файлов DEF-9xx.xlsx и numbers.xlsx
def_data = pd.read_excel('Data.xlsx')
numbers_data = pd.read_excel('numbers.xlsx')

# Создание пустого списка для хранения сопоставленных данных
mapped_data = []

# Итерация по каждому номеру из файла numbers.xlsx

for number in numbers_data['Numbers']:
    # Получение кода оператора (АБС) и номера для диапазона
    x = str(number)
    kod_operatora = x[1:4]
    nomer =  x[4:11]

    # Поиск соответствующего диапазона значений "От" и "До"
    
    match = def_data[(def_data['АВС/ DEF'] == int(kod_operatora)) & (def_data['От'] <= int(nomer)) & (def_data['До'] >= int(nomer))]

    
    # Проверка, найдено ли совпадение
    if not match.empty:
        # Получение значений оператора и региона для найденного диапазона
        operator = match['Оператор'].iloc[0]
        region = match['Регион'].iloc[0]
        
        # Добавление сопоставленных данных в список
        mapped_data.append([number, operator, region])

# Создание DataFrame для сопоставленных данных
mapped_df = pd.DataFrame(mapped_data, columns=['Номер', 'Оператор сотовой связи', 'Регион'])

# Сохранение DataFrame в новый файл output.xlsx
mapped_df.to_excel('output.xlsx', index=False)
