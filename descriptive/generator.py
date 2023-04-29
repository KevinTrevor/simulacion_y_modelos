from random import randint

ages_list = [randint(22, 47) for i in range(1000)]

with open(file="descriptive/data.csv",mode="w") as file:
    file.write("Edad" + "\n")
    for age in ages_list:
         file.write(str(age) + "\n")