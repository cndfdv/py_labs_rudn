import random

with open("./second_lab/text.txt", "w") as file:
    for i in range(10):
        file.write(
            str(random.randint(1, 31))
            + "."
            + str(random.randint(1, 12))
            + "."
            + str(random.randint(2020, 2026)) 
            + "\n"
        )
