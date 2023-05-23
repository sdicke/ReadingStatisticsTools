import re
import sys
from statistics import mean
from statistics import median

pattern = re.compile("\([0-9]*\)")
year = sys.argv[1]

numbers = []
prefix = "";
input = open(" " + prefix + ".md")
for line in input:
	length = re.findall(pattern, line)[0][1:-1]
	length = int(length)
	numbers.append(length)

average = mean(numbers)
average = round(average)
print("Average:")
print(average)
med = median(numbers)
print("Median:")
print(med)
total = sum(numbers)
print("Sum:")
print(total)