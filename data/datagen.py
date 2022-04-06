import random
lines = ""

for i in range(1, 15):
    # add PID
    lines += str(i) + ","
    for n in range(1, random.randrange(1, 10)):
        # add CPU time
        lines += str(random.randrange(1, 10)) + ","
        # add IO time
        lines += str(random.randrange(1, 10)) + ","

    lines += "\n"

# write to file
with open("data2.csv", "w") as f:
    f.write(lines)
