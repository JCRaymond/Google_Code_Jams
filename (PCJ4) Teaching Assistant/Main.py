from Utils.CJFileIO import *

f = CJFileIO(size=CJSize.large)

for days in [f.readln() for t in range(f.readi())]:

    grade = 0

    while True:
        i = days.find("CC") if days.find("CC") != -1 else days.find("JJ")
        if i == -1: break
        days = days[:i] + days[i+2:]
        grade += 10

    f.write_next_case(grade + len(days)/2*5)

f.close()