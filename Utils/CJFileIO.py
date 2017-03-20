from enum import Enum


class CJSize(Enum):
    small = "small"
    large = "large"
    test = "test"


class CJFileIO:

    def __init__(self, problem = "A",size = CJSize.small, pracnum = None):
        if type(size) is not CJSize:
            raise TypeError("The parameter must be of type CJSize")

        file_in = "Files/" + problem + "-" + size.value + "-practice" + ("" if pracnum == None else ("-" + str(pracnum))) + ".in"
        file_out = "Files/" + size.value + "-out" + ("" if pracnum == None else ("-" + str(pracnum))) + ".out"
        self.__fin = open(file_in, "r")
        self.__fout = open(file_out, "w")

        self.__buff = []
        self.__case = 1
        self.__last_case_done = True

    def read(self):
        if len(self.__buff) == 0:
            self.__buff = self.readln().split(" ")

        ret = self.__buff[0]
        self.__buff = self.__buff[1:]
        return ret

    def readi(self):
        return int(self.read())

    def readln(self):
        self.__buff = []
        return self.__fin.readline().strip("\n")

    def write_next_case(self, case = ""):
        if not self.__last_case_done:
            self.write("\n")
        self.write("Case #" + str(self.__case) + ": " + str(case))
        self.__last_case_done = False
        self.__case += 1

    def write(self, line):
        self.__fout.write(str(line))

    def writeln(self, line = ""):
        self.__fout.write(str(line) + "\n")
        self.__last_case_done = True

    def close(self):
        self.__fin.close()
        self.__fout.close()