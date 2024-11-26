
#HW PTS TOTAL
hw = {
    1: [ 56, 60],
    2: [ 88, 92],
    3: [ 69, 70],
    4: [ 60, 60],
    5: [ 70, 70],
    6: [ 82, 82],
    7: [ 44, 45],
    8: [ 72, 72],
    9: [ 60, 60],
    10:[ 77, 78],
    11:[ 78, 78],
    12:[ 80, 80],
}

count = len(hw)
print(count)

gsum = []

for n,res in hw.items():
    pi,ptot = res
    g = pi / ptot
    gsum.append(g)
    print(f"HW #{n:2d}: {pi:3d}/{ptot:3d} = {g*100:10.2f}%")

hw_grade = sum(gsum)/count
print(f"HW grade: {hw_grade*100:10.1f} %")



grades = {
    "HW": (hw_grade, 0.33),
    "MID": (0.915, 0.33),
    "FINAL": (0.80, 0.34),
}

class_grade = 0

for k,v in grades.items():
    g,per = v
    class_grade += g*per

print(f"class grade: {class_grade}")
