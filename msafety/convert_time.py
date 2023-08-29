import datetime

#readfile and writefile paths
readfile = "C:/Users/hi/Desktop/msafety.txt"
writefile = "C:/Users/hi/Desktop/msafety unix.txt"

# Opens readfile and writefile
with open(readfile, 'r') as input_file, open(writefile, 'w') as output_file:
    # Loops over each line in the input file
    for line in input_file:
        # Extracts the date, time, and heart rate from the rows
        date_time, heart_rate = line.strip().split(' ')
        date, time = date_time.split('T')
        
        # Converts the date and time in the file to Unix format
        dt = datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S%z')
        unix_time = int(dt.timestamp())

        # Writes the Unix time and heart rate to the writefile
        output_file.write(f'{unix_time} {heart_rate}\n')

