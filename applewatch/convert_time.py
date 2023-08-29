#script that converts the date and time to the UNIX time format alongside the collected heartbeat for that specific time
import time
#path variables
readfile = "C:/Users/hi/Desktop/applewatch.txt"
writefile = "C:/Users/hi/Desktop/applewatch unix.txt"

#the 3 important variables to convert to the unix time
date_str = input("Enter the date in YYYY-MM-DD format: ")
start_time_str = input("Enter the start time in HH:MM:SS format: ")
duration_str = input("Enter the duration in HH:MM:SS format: ")

# Converts start time and duration (length) to seconds
start_time_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time_str.split(":")))
duration_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], duration_str.split(":")))

# Converts date and start time to UNIX timestamp
start_timestamp = int(time.mktime(time.strptime(date_str + " " + start_time_str, "%Y-%m-%d %H:%M:%S")))

# Opens input file and reads all the rows, but starting from row 10, because row 1-9 doesnt include the heartbeat data, it only includes general info
with open(readfile, "r") as input_file:
    #starting from row 9
    #saves the desired data to the rows variable
    rows = input_file.readlines()[9:]

# Creates a new .txt file for output, the name it gets is from the "writefile" variable in the first rows of code
with open(writefile, "w") as output_file:
    # Writes title to the writefile
    
    # Iterates through all the rows in the "rows" variable and writes the UNIX timestamp and heartbeats to the output file (writefile)
    for row in rows:
        # Calculates UNIX timestamp for the current row we are in
        unix_timestamp = start_timestamp + (duration_sec / len(rows))
        
        # Writes UNIX timestamp and heartbeat to output file and goes to next row
        output_file.write("{:.0f} ".format(unix_timestamp) + row.strip() + "\n")
        
        # Updates start timestamp for the next row
        start_timestamp = unix_timestamp