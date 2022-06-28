#!/usr/bin/python3

import psutil
import sys
import os

if len(sys.argv) != 2 and len(sys.argv) !=3 :
  print("Usage: {} PID SAMPLING_TIME [SAVE_FILENAME]".format(sys.argv[0]))
  print("       PID: Process ID to be checked")
  print("       SAMPLING_TIME: sampling time (minute)")
  print("       SAVED_FILENAME: recorded data filename")
  sys.exit(1)

pid = sys.argv[1]
sampling_time = sys.argv[2]
save_filename = 'recorded_data.csv'
if sys.argv[3] :
  save_filename = sys.argv[3]

print("Pid: {}, Time: {}m".format(pid, sampling_time))

process = psutil.Process(int(pid))

test_result = []

check_number = int(sampling_time) * 60 # interval is 1s

for _ in range(0, check_number, 1):
  test_result.append(process.cpu_percent(1))

summary = 0
for item in test_result:
  summary += item

average_cpu_usage = summary / len(test_result)
print("CPU usage: {:.0%} in {} minutes".format(average_cpu_usage, sampling_time))

print("Total recorded data: {}".format(len(test_result)))
with open(save_filename, 'w') as f:
  for cpu_usage in test_result:
    f.write('{},'.format(cpu_usage))

# Remove last ','
with open(save_filename, 'rb+') as f:
  f.seek(-1, os.SEEK_END)
  f.truncate()

print("Save recorded data into {}.".format(save_filename));


