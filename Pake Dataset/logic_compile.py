import pandas as pd
import numpy as np
import prettytable as prettytable
import random as rnd

df = pd.read_excel(
    'D:\Kuliah\Skripsi\skripsi\Pake Dataset\dataset\Data.xlsx')
dw = pd.read_excel(
    'D:\Kuliah\Skripsi\skripsi\Pake Dataset\dataset\TetapanWaktu.xlsx')
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
dictionarydosen = {}
while j < totalsemester:
    table = prettytable.PrettyTable(
        ['Semester ' + str(j), 'Nama dosen'])
    data = df.where(df['Semester'] == j).dropna()
    arr = data.values.tolist()
    for i in range(len(arr)):
        hitung = arr[i]
        # semester berapa
        if j == 1:
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
            # hari = hitung[3]
            # starttime = hitung[4]
            # endtime = hitung[5]
            # gabungan = hari+' ' + starttime+' - ' + endtime
            # if gabungan not in penampungwaktu:
            #     idwaktu = "MT" + str(countwaktu)
            #     t = [idwaktu]
            #     penampungwaktu.append(gabungan)
            #     t.append(gabungan)
            #     t.append(hitung[10])
            #     waktu.append(t)
            #     countwaktu = countwaktu + 1
            # k = hitung[8]
            # cari kode mata kuliah
            if [hitung[8]] not in kode:
                kode.append([hitung[8]])
            # cari matakuliah berdasarkan kode
            # if [hitung[8]] in kode:
            #     if [hitung[1]] not in matakuliah:
            #         matakuliah.append([hitung[1]+" " + hitung[2]])
            #         matakuliahdandosen.append(
            #             [hitung[1]+" " + hitung[2], [hitung[0]], hitung[8], hitung[9], hitung[10], hitung[7]])
            #     else:
            #         indeks = matakuliah.index([hitung[1]])
            #         if hitung[0] not in matakuliahdandosen[indeks][1]:
            #             matakuliahdandosen[indeks][1].append(hitung[0])
            if [hitung[8]] in kode:
                temp = str(hitung[1])
                matakuliahdandosen.append(
                    [temp, [], hitung[8], hitung[9], hitung[10], hitung[7], hitung[2]])
                if hitung[1] not in dictionarydosen:
                    dictionarydosen[hitung[1]] = [hitung[0]]
                elif hitung[0] not in dictionarydosen[hitung[1]]:
                    dictionarydosen[hitung[1]].append(hitung[0])

        table.add_row([arr[i], hitung[0]])
    # print(table)
    j += 1
for i in range(len(matakuliahdandosen)):
    idcourse = "C" + str(i)
    matakuliahdandosen[i].append(idcourse)

dw.dropna()
datawaktu = dw.values.tolist()

for i in range(len(datawaktu)):
    hitung = datawaktu[i]
    hari = hitung[0]
    starttime = hitung[1]
    endtime = hitung[2]
    sks = hitung[3]
    gabungan = hari+' ' + str(starttime)+' - ' + str(endtime)
    if gabungan not in penampungwaktu:
        idwaktu = "MT" + str(countwaktu)
        t = [idwaktu]
        penampungwaktu.append(gabungan)
        t.append(gabungan)
        t.append(sks)
        t.append(starttime)
        t.append(endtime)
        t.append(hari)
        waktu.append(t)
        countwaktu = countwaktu + 1
iterator = 0
indeks = 0
while iterator < len(matakuliahdandosen):
    for key, value in dictionarydosen.items():
        if key in matakuliahdandosen[iterator][0]:
            kunci = key
            break
    matakuliahdandosen[iterator][1] = dictionarydosen[kunci]
    iterator = iterator + 1
# print(datawaktu)
# for i in range(len(datawaktu)):
# print(datawaktu[i][0])
# print(table)
print(waktu)
# print('\n')
# print(dosen)
# print('\n')
# print(kelas)
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
# print(dictionarydosen)
# for i in range(len(matakuliahdandosen)):
#     print(matakuliahdandosen[i], "\n")
