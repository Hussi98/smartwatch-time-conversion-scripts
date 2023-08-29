import json
import os
import re
from datetime import datetime

input_folder = "C:/Users/hi/Desktop/exjobb/jsonfiles"
output_file = "C:/Users/hi/Desktop/sortedjson.txt"


with open(output_file, "w") as f:
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            with open(os.path.join(input_folder, file_name)) as json_file:
                try:
                    data = json.load(json_file)
                    for hr_data in data["heartrate"]:
                        date_time = hr_data["time"]
                        heartbeat = hr_data["data"]
                        f.write(f"{date_time} {heartbeat}\n")
                except KeyError:
                    print(f"Error: {file_name} does not contain 'heartrate' data")
