import time

#readfile and writefile paths
readfile = "C:/Users/hi/Desktop/fitbit.txt"
writefile = "C:/Users/hi/Desktop/fitbit unix.txt"

#script that converts the date and time to the UNIX time format alongside the collected heartbeat for that specific time

# Asks for the date in the following format: YYYY-MM-DD and saves the user input in the variable date_str
date_str = input("Enter the date (YYYY-MM-DD): ")

# function to convert time in hh:mm:ss from the desired file to UNIX time and returns the unix time
def to_unix_time(time_str):
    time_struct = time.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M:%S")
    unix_time = int(time.mktime(time_struct))
    return unix_time

# Opens the file containing rows of the time in the format of hh:mm:ss and the heartbeat
with open(readfile, "r") as input_file:
    # Opens the file to write the UNIX time followed by the heartbeat
    with open(writefile, "w") as output_file:
        # Loops through each line in the input file
        for line in input_file:
            # Splits the line into time and heartbeat
            time_str, heartbeat = line.strip().split(",")
            # Converts the time to UNIX time
            unix_time = to_unix_time(time_str)
            # Writes the UNIX time and heartbeat to the output file
            output_file.write(str(unix_time) + " " + heartbeat + "\n")
