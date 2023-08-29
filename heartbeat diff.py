#test script to check if 2 files have same unix time, if yes, get their heartrate difference and compute to another txt file

# import  libraries
import csv

# paths to the 2 files (read)
readfile1 =   "C:/Users/hi/Desktop/polar band unix 1.txt"
readfile2 =   "C:/Users/hi/Desktop/fitbit unix 1.txt"

#path to the output files (write)
output_file = "C:/Users/hi/Desktop/fitbit/heartbeat difference.txt"

# creates empty dictionary to store heart rates with unix time
heart_rates = {}

# reads data from file1 and add to dictionary
with open(readfile1, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        unix_time, heart_rate = int(row[0]), int(row[1])
        heart_rates[unix_time] = [heart_rate]

# reads data from file2 and append to dictionary
with open(readfile2, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        unix_time, heart_rate = int(row[0]), int(row[1])
        if unix_time in heart_rates:
            heart_rates[unix_time].append(heart_rate)
        else:
            heart_rates[unix_time] = [heart_rate]

# computes and writes differences in heartbeat for that specific unix time to the output file (writefile)
with open(output_file, 'w') as f:
    for unix_time, rates in heart_rates.items():
        if len(rates) == 2:
            diff = abs(rates[0] - rates[1])
            f.write(f'{unix_time} {diff}\n')