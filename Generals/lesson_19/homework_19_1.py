from datetime import datetime
import logging

def filter_lines_by_key(filename, key):
    with open(filename, "r") as f:
        lines = f.readlines()

    filtered_lines = []
    for line in lines:
        if key in line:
            filtered_lines.append(line)

    return filtered_lines

filename = "hblog.txt"
key = "Key TSTFEED0300|7E3E|0400"

filtered_lines = filter_lines_by_key(filename, key)


def extract_time(line):
    position = line.find("Timestamp ")
    time_start = position +len("Timestamp ")
    time_text = line[time_start:time_start + 8]
    time_object = datetime.strptime(time_text, "%H:%M:%S")
    return time_object


logging.basicConfig(filename="hb_test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def analyze_heartbeats(filtered_lines):
    for i in range(len(filtered_lines) - 1):
        current_line = filtered_lines[i]
        next_line = filtered_lines[i + 1]

        current_time = extract_time(current_line)
        next_time = extract_time(next_line)

        diff = (current_time - next_time).total_seconds()

        if 31 < diff < 33:
            logging.warning(f"Heartbeat WARNING at {current_time.time()}: gap = {diff} sec")
        elif diff >=33:
            logging.error(f"Heartbeat ERROR at {current_time.time()}: gap = {diff} sec")

analyze_heartbeats(filtered_lines)