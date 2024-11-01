
import pandas as pd
import os
folder_path = 'C:\\Users\\felle\\OneDrive\\Рабочий стол\\ml_sammm'

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
csv_files


len(csv_files)

df_list = []
for file in csv_files:
    try:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path, sep=';')
        print(df.head())
        df_list.append(df)
    except:
        print(file_path)

len(df_list)

df_list.append(pd.read_csv('C:\\Users\\felle\\OneDrive\\Рабочий стол\\новая'))


for df_ in df_list:
    df_all = pd.concat(df_list, ignore_index=True )
df_all    

df_all.drop_duplicates(inplace=True, ignore_index=True)
df_all.shape

df_all['location'].value_counts()
df_all = df_all.drop_duplicates()
df_all.to_csv('C:\\Users\\felle\\OneDrive\\Рабочий стол\\ml_sammm\\started.py', index=False)