import time
import prettytable as prettytable
import random as rnd
import pandas as pd


POPULATION_SIZE = 10
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 0.33 * POPULATION_SIZE
MUTATION_RATE = 0.1

df = pd.read_excel(
    'D:\Kuliah\Skripsi\skripsi\Pake Dataset\dataset\Data.xlsx')
dw = pd.read_excel(
    'D:\Kuliah\Skripsi\skripsi\Pake Dataset\dataset\TetapanWaktu.xlsx')

# print(df.head())
# print(dw.head())

currentsemester = 1
totalsemester = 8
countdosen = 1
countwaktu = 1
dosen = []
matakuliah = []
waktu = []
kode = []
nd = []
nk = []
t = []
penampungdosen = []
penampungwaktu = []
penampungkode = []
penampungmatakuliah = []
penampungdosen = []
penampungdosenajar = []
matakuliahdandosen = []
dictionarydosen = {}
while currentsemester < totalsemester:
    data = df.where(df['Semester'] == currentsemester).dropna()
    arr = data.values.tolist()
    for i in range(len(arr)):
        hitung = arr[i]
        # semester berapa
        if currentsemester == 1:
            if hitung[0] not in penampungdosen:
                iddosen = "I" + str(countdosen)
                nd = [iddosen]
                penampungdosen.append(hitung[0])
                nd.append(hitung[0])
                dosen.append(nd)
                countdosen = countdosen + 1
            if [hitung[8]] not in kode:
                kode.append([hitung[8]])
            if [hitung[8]] in kode:
                temp = str(hitung[1])
                matakuliahdandosen.append(
                    [temp, [], hitung[8], hitung[9], hitung[10], hitung[7], hitung[2]])
                if hitung[1] not in dictionarydosen:
                    dictionarydosen[hitung[1]] = [hitung[0]]
                elif hitung[0] not in dictionarydosen[hitung[1]]:
                    dictionarydosen[hitung[1]].append(hitung[0])
    currentsemester += 1
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
    gabungan = hari+' ' + str(starttime)+':00 - ' + str(endtime) + ':00'
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

iteratormatakuliahdandosen = 0
while iteratormatakuliahdandosen < len(matakuliahdandosen):
    for key, value in dictionarydosen.items():
        if key in matakuliahdandosen[iteratormatakuliahdandosen][0]:
            kunci = key
            break
    matakuliahdandosen[iteratormatakuliahdandosen][1] = dictionarydosen[kunci]
    iteratormatakuliahdandosen = iteratormatakuliahdandosen + 1


class Data:
    # ROOMS = kelas
    MEETING_TIMES = waktu
    INSTRUCTORS = dosen

    def __init__(self):
        # self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        namadosen = []
        gabunglistpengajar = []
        newarraycourse = []
        kodedepartment = []
        departmentdancourse = []
        newarraydept = []
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1], self.MEETING_TIMES[i]
                                                  [2], self.MEETING_TIMES[i][3], self.MEETING_TIMES[i][4], self.MEETING_TIMES[i][5]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(
                self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        for i in range(len(dosen)):
            namadosen.append(dosen[i][1])
        for i in range(len(matakuliahdandosen)):
            listpengajar = []
            for j in range(len(matakuliahdandosen[i][1])):
                if matakuliahdandosen[i][1][j] in namadosen:
                    penandacourse = namadosen.index(
                        matakuliahdandosen[i][1][j])
                    listpengajar.append(self._instructors[penandacourse])
            gabunglistpengajar.append(listpengajar)
        for i in range(len(matakuliahdandosen)):
            course = Course(
                matakuliahdandosen[i][7], matakuliahdandosen[i][0], gabunglistpengajar[i], 30, matakuliahdandosen[i][3], matakuliahdandosen[i][4], matakuliahdandosen[i][5], matakuliahdandosen[i][6])
            newarraycourse.append(course)
            if matakuliahdandosen[i][2] not in kodedepartment:
                kodedepartment.append(matakuliahdandosen[i][2])
                departmentdancourse.append(
                    [matakuliahdandosen[i][2], [course]])
            else:
                departindeks = kodedepartment.index(matakuliahdandosen[i][2])
                if course not in matakuliahdandosen[departindeks][1]:
                    departmentdancourse[departindeks][1].append(course)
        self._courses = newarraycourse
        for i in range(len(departmentdancourse)):
            dept = Department(
                departmentdancourse[i][0], departmentdancourse[i][1])
            newarraydept.append(dept)
        self._depts = newarraydept
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts

    def get_meetingTimes(self):
        return self._meetingTimes

    def get_meetingTimesbySKS(self, datasks):
        sortbysks = []
        for i in range(len(self._meetingTimes)):
            if (self._meetingTimes[i].get_sks() == datasks):
                sortbysks.append(self._meetingTimes[i])
        return sortbysks

    def get_numberOfClasses(self): return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimesbySKS(courses[j].get_sks()
                                                                    )[rnd.randrange(0, len(data.get_meetingTimesbySKS(courses[j].get_sks())))])
                newClass.set_instructor(courses[j].get_instructors(
                )[rnd.randrange(0, len(courses[j].get_instructors()))])
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            for j in range(0, len(classes)):
                if (j >= i):
                    if(classes[i].get_instructor() == classes[j].get_instructor() and classes[i].get_course().get_kelas() != classes[j].get_course().get_kelas() and classes[i].get_course().get_smst()):
                        if(classes[i].get_meetingTime() == classes[j].get_meetingTime()):
                            self._numbOfConflicts += 1
                        if(classes[i].get_meetingTime().get_day() == classes[j].get_meetingTime().get_day()):
                            if(classes[i].get_meetingTime().get_start() == classes[j].get_meetingTime().get_start()):
                                self._numbOfConflicts += 1
                            if(classes[i].get_meetingTime().get_start() > classes[j].get_meetingTime().get_start()
                                    and classes[i].get_meetingTime().get_end() > classes[j].get_meetingTime().get_start()
                                    and classes[i].get_meetingTime().get_start() != classes[j].get_meetingTime().get_end()):
                                self._numbOfConflicts += 1
                            if(classes[i].get_meetingTime().get_start() < classes[j].get_meetingTime().get_start()
                                    and classes[i].get_meetingTime().get_end() > classes[j].get_meetingTime().get_start()):
                                self._numbOfConflicts += 1
                    if(classes[i].get_course().get_smst() == classes[j].get_course().get_smst() and classes[i].get_course().get_name() != classes[j].get_course().get_name()):
                        if(classes[i].get_course().get_kelas() == classes[j].get_course().get_kelas() or classes[i].get_course().get_kelas() in classes[j].get_course().get_kelas()):
                            if(classes[i].get_meetingTime() == classes[j].get_meetingTime()):
                                self._numbOfConflicts += 1
                            if(classes[i].get_meetingTime().get_day() == classes[j].get_meetingTime().get_day()):
                                if(classes[i].get_meetingTime().get_start() == classes[j].get_meetingTime().get_start()):
                                    self._numbOfConflicts += 1
                                if(classes[i].get_meetingTime().get_start() > classes[j].get_meetingTime().get_start()
                                   and classes[i].get_meetingTime().get_end() > classes[j].get_meetingTime().get_start()
                                   and classes[i].get_meetingTime().get_start() != classes[j].get_meetingTime().get_end()):
                                    self._numbOfConflicts += 1
                                if(classes[i].get_meetingTime().get_start() < classes[j].get_meetingTime().get_start()
                                   and classes[i].get_meetingTime().get_end() > classes[j].get_meetingTime().get_start()):
                                    self._numbOfConflicts += 1
        return 1 / ((1.0*self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())

    def get_schedules(self): return self._schedules


class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(
        self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[
                0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[
                0]
            crossover_pop.get_schedules().append(
                self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5):
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(
                pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()):
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule


class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents, tipe, sks, smst, kelas):
        self._kelas = kelas
        self._smst = smst
        self._number = number
        self._name = name
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors
        self._tipe = tipe
        self._sks = sks

    def get_kelas(self): return self._kelas
    def get_smst(self): return self._smst
    def get_sks(self): return self._sks
    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def get_tipe(self): return self._tipe
    def __str__(self): return self._name


class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name


class Room:
    def __init__(self, number, seatingCapacity, tipe):
        self._number = number
        self._seatingCapacity = seatingCapacity
        self._tipe = tipe

    def get_tipe(self): return self._tipe
    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity


class MeetingTime:
    def __init__(self, id, time, sks, start, end, day):
        self._day = day
        self._start = start
        self._end = end
        self._sks = sks
        self._id = id
        self._time = time

    def get_day(self): return self._day
    def get_start(self): return self._start
    def get_end(self): return self._end
    def get_sks(self): return self._sks
    def get_id(self): return self._id
    def get_time(self): return self._time


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self): return self._name
    def get_courses(self): return self._courses


class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._instructor.get_id()
                                                      ) + "," + str(self._meetingTime.get_id())


class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        Tabulatedepts = []
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row(
                [depts.__getitem__(i).get_name(), tempStr])
            Tabulatedepts.append(
                [depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(
            ['id', 'course #', 'instructors'])
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name()+" " + courses[i].get_kelas(), tempStr])
        print(availableCoursesTable)
        # print(tabulate(Tabulatecourse, headers=[
        #       'id', 'course #', 'max # of students', 'instructors']))

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(
            ['id', 'instructor'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row(
                [instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(
            ['id', 'Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,instructor,meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i), round(schedules[i].get_fitness(
            ), 3), schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            ['Class #', 'Dept', 'Course (kelas, semester, sks)', 'Instructor (Id)',  'Meeting Time (Id,start,end)'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_kelas() + ", " +
                           str(classes[i].get_course(
                           ).get_smst()) + ", " + str(classes[i].get_course().get_sks()) + ")",
                           #                classes[i].get_room().get_number(
                           # ) + " (" + str(classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name(
            ) + " (" + str(classes[i].get_instructor().get_id()) + ")",
                classes[i].get_meetingTime().get_time() + " (" + str(classes[i].get_meetingTime().get_id()) + ", " + str(classes[i].get_meetingTime().get_start()) + ", " + str(classes[i].get_meetingTime().get_end()) + ")"])
        print(table)


start_time = time.time()
data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # "+str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
while (population.get_schedules()[0].get_fitness() != 1.0):
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    # if generationNumber == 100:
    #     break
    # displayMgr.print_generation(population)
    # displayMgr.print_schedule_as_table(population.get_schedules()[0])
displayMgr.print_schedule_as_table(population.get_schedules()[0])
print("\n> Generation # " + str(generationNumber))
print("%s seconds" % (time.time() - start_time))
print("\n\n")
