readfile = "C:/Users/hi/Desktop/polar band.txt"
writefile = "C:/Users/hi/Desktop/polar band unix.txt"
#script that converts the date and time to the UNIX time format alongside the collected heartbeat for that specific time
import csv
import time

# Opens the CSV file for reading
with open(readfile, 'r') as csvfile:

    # Opens the output file for writing
    with open(writefile, 'w') as outfile:

        # Loops over the rows in the CSV file
        reader = csv.reader(csvfile)
        for row in reader:

            # Parses the date/time value and convert it to Unix time
            dt = time.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
            unix_time = int(time.mktime(dt))

            # Writes the Unix time and heart rate to the output file
            outfile.write(str(unix_time) + ' ' + row[1] + '\n')
