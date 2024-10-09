
#HW PTS TOTAL
hw = {
    1: [ 56, 60],
    2: [ 88, 92],
    3: [ 69, 70],
    4: [ 60, 60],
    5: [ 70, 70],
    6: [ 82, 82],
    7: [ 44, 45],
}

count = len(hw)
print(count)

gsum = []

for n,res in hw.items():
    pi,ptot = res
    g = pi / ptot
    gsum.append(g)
    print(f"HW #{n:2d}: {pi:3d}/{ptot:3d} = {g*100:10.2f}%")

grade = sum(gsum)/count
print(f"HW grade: {grade*100:10.1f} %")


