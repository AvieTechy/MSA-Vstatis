import csv

# File path
file_path = (
    "/home/aaronpham5504/personalFolder/MSA/Project/MSA-Vstatis/Data/Score_y.csv"
)

# Initialize counters
count_0 = 0
count_1 = 0
count_2 = 0

# Read the file and count occurrences of 0, 1, and 2
with open(file_path, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            if value == "0":
                count_0 += 1
            elif value == "1":
                count_1 += 1
            elif value == "2":
                count_2 += 1

# Print the results
print(f"Count of 0: {count_0}")
print(f"Count of 1: {count_1}")
print(f"Count of 2: {count_2}")
