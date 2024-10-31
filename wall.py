
import pandas as pd
import os

# Укажите путь к папке с CSV-файлами
folder_path = r"C:\\Users\\felle\\OneDrive\\Рабочий стол\\ml_samm"

# Получаем список всех CSV-файлов в папке
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Список для хранения DataFrame
df_list = []

# Читаем каждый CSV-файл и добавляем его в список
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path, sep=',', encoding='utf-16')  # Укажите нужную кодировку
        df_list.append(df)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")

# Объединяем все DataFrame в один
df_all = pd.concat(df_list, ignore_index=True)

# Сохраняем объединенный DataFrame в новый CSV-файл
output_file_path = os.path.join(folder_path, 'merged_data.csv')
df_all.to_csv(output_file_path, index=False)

print(f"Все данные успешно собраны в файл: {output_file_path}")
