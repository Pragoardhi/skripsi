import pandas as pd
import numpy as np
import prettytable as prettytable
import random as rnd

df = pd.read_excel(
    'D:\Kuliah\Skripsi\Project Skripsi\dataset\Data.xlsx')
j = 1
totalsemester = 8
count = 1
namadosen = []
kelas = []
nd = []
nk = []
penampungkelas = []
penampungdosen = []
while j < totalsemester:
    table = prettytable.PrettyTable(
        ['Semester ' + str(j), 'Nama dosen'])
    data = df.where(df['Semester'] == j).dropna()
    arr = data.values.tolist()
    for i in range(len(arr)):
        hitung = arr[i]
        if j == 1:
            if hitung[0] not in penampungdosen:
                # print(nd)
                id = "I" + str(count)
                nd = [hitung[0]]
                penampungdosen.append(hitung[0])
                nd.append(id)
                namadosen.append(nd)
                count = count + 1
            if hitung[6] not in penampungkelas:
                # print('ketemu')
                # print(hitung[6])
                seat = 30
                nk = [hitung[6]]
                penampungkelas.append(hitung[6])
                nk.append(seat)
                kelas.append(nk)

        table.add_row([arr[i], hitung[0]])
    j += 1
#     print(table)
print(namadosen)
print('\n')
print(kelas)

# print(kelas[0])
# print(hitung[6])
