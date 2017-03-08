from enum import Enum


class CJSize(Enum):
    small = "small"
    large = "large"
    test = "test"


class CJFileIO:

    def __init__(self, problem = "A",size = CJSize.small):
        if type(size) is not CJSize:
            raise TypeError("The parameter must be of type CJSize")

        file_in = "Files/" + problem + "-" + size.value + "-practice.in"
        file_out = "Files/" + size.value + "-out.out"
        self.__fin = open(file_in, "r")
        self.__fout = open(file_out, "w")

        self.__buff = []
        self.case = 1

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
        return self.__fin.readline()[:-1]

    def write_next_case(self, case = ""):
        self.__fout.write("Case #" + str(self.case) + ": " + str(case) + "\n")
        self.case += 1

    def write(self, line):
        self.__fout.write(str(line))

    def writeln(self, line = ""):
        self.__fout.write(str(line) + "\n")

    def close(self):
        self.__fin.close()
        self.__fout.close()