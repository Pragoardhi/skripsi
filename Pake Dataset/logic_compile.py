import pandas as pd
import numpy as np
import prettytable as prettytable
import random as rnd

df = pd.read_excel(
    'D:\Kuliah\Skripsi\skripsi\Pake Dataset\dataset\Data.xlsx')
j = 1
totalsemester = 8
countdosen = 1
countwaktu = 1
dosen = []
matakuliah = []
kelas = []
waktu = []
kode = []
nd = []
nk = []
t = []
penampungkelas = []
penampungdosen = []
penampungwaktu = []
penampungkode = []
penampungmatakuliah = []
penampungdosen = []
penampungdosenajar = []
matakuliahdandosen = []
while j < totalsemester:
    table = prettytable.PrettyTable(
        ['Semester ' + str(j), 'Nama dosen'])
    data = df.where(df['Semester'] == j).dropna()
    arr = data.values.tolist()
    for i in range(len(arr)):
        hitung = arr[i]
        # semester berapa

        if hitung[0] not in penampungdosen:
            # print(nd)
            iddosen = "I" + str(countdosen)
            nd = [iddosen]
            penampungdosen.append(hitung[0])
            nd.append(hitung[0])
            dosen.append(nd)
            countdosen = countdosen + 1
        if hitung[6] not in penampungkelas:
            # print('ketemu')
            # print(hitung[6])
            seat = 30
            nk = [hitung[6]]
            penampungkelas.append(hitung[6])
            nk.append(seat)
            nk.append(hitung[9])
            kelas.append(nk)
        hari = hitung[3]
        starttime = hitung[4]
        endtime = hitung[5]
        gabungan = hari+' ' + starttime+' - ' + endtime
        if gabungan not in penampungwaktu:
            idwaktu = "MT" + str(countwaktu)
            t = [idwaktu]
            penampungwaktu.append(gabungan)
            t.append(gabungan)
            waktu.append(t)
            countwaktu = countwaktu + 1
        k = hitung[8]
        # cari kode mata kuliah
        if [hitung[8]] not in kode:
            kode.append([hitung[8]])
        # cari matakuliah berdasarkan kode
        if [hitung[8]] in kode:
            if [hitung[1]] not in matakuliah:
                matakuliah.append([hitung[1]])
                matakuliahdandosen.append(
                    [hitung[1], [hitung[0]], hitung[8], hitung[9]])
            else:
                indeks = matakuliah.index([hitung[1]])
                if hitung[0] not in matakuliahdandosen[indeks][1]:
                    matakuliahdandosen[indeks][1].append(hitung[0])
    table.add_row([arr[i], hitung[0]])

    j += 1
for i in range(len(matakuliahdandosen)):
    idcourse = "C" + str(i)
    matakuliahdandosen[i].append(idcourse)
# print(table)
# print(waktu)
# print('\n')
# print(dosen)
# print('\n')
print(kelas)
# print('\n')
# print(kode)
# print('\n')
# print(matakuliah)
# print('\n')
# print(penampungdosenajar)
# print('\n')
# print(matakuliahdandosen)

# gabunglistpengajar = []
# for i in range(len(dosen)):
#     namadosen.append(dosen[i][1])

# for i in range(len(matakuliahdandosen)):
#     listpengajar = []
#     for j in range(len(matakuliahdandosen[i][1])):
#         if matakuliahdandosen[i][1][j] in namadosen:
#             penandacourse = namadosen.index(matakuliahdandosen[i][1][j])
#             listpengajar.append(self._instructors[penandacourse])
#     gabunglistpengajar.append(listpengajar)
