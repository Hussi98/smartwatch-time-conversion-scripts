from collections import defaultdict
import math

# this script checks if the file has more than one same unix time, if it does, calculates their mean heartbeats and removed the duplicate unix time
# paths
#readfile = "C:/Users/hi/Desktop/polar band unix.txt"
#writefile = "C:/Users/hi/Desktop/polar band unix.txt"

readfile = "C:/Users/hi/Desktop/xiaomi unix.txt"
writefile = "C:/Users/hi/Desktop/xiaomi unix.txt"

# creates a dictionary to store heartbeats for each unix time format
heartbeats_by_unixtime = defaultdict(list)

# reads the input file and gives data to the dictionary
with open(readfile, "r") as f:
    for line in f:
        unixtime, heartbeat = map(int, line.strip().split())
        heartbeats_by_unixtime[unixtime].append(heartbeat)

# creates a list to store the new desired rows
new_rows = []

# goes through over the dictionary and compute the mean heartbeat for each unix time
for unixtime, heartbeats in heartbeats_by_unixtime.items():
    # if there are multiple heartbeats for this specific unix time
    if len(heartbeats) > 1:  
        #mean_heartbeat = round(sum(heartbeats) / len(heartbeats))  # computes the mean heartbeat
        mean_heartbeat = math.ceil(sum(heartbeats) / len(heartbeats))  # computes the mean heartbeat and rounds up
        new_rows.append((unixtime, mean_heartbeat))  # adds the new row to the list
    else:
        new_rows.append((unixtime, heartbeats[0]))  # adds the existing row to the list

# sorts the new rows by unix time
new_rows.sort()

# writes the new rows to the output file
with open(writefile, "w") as f:
    for row in new_rows:
        f.write(f"{row[0]} {row[1]}\n")
