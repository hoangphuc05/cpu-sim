import random
lines = ""

for i in range(1, 15):
    # add PID
    lines += str(i) + ","
    for n in range(1, random.randrange(1, 50)):
        # add CPU time
        lines += str(random.randrange(1, 50)) + ","
        # add IO time
        lines += str(random.randrange(1, 50)) + ","

    lines += "\n"

# write to file
with open("data_long.csv", "w") as f:
    f.write(lines)
