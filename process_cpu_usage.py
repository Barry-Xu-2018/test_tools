import psutil
import sys

pid = sys.argv[1]
check_time = sys.argv[2]

print("Pid: {}, Time: {}m".format(pid, check_time))

process = psutil.Process(int(pid))

test_result = []

check_number = int(check_time) * 60 # interval is 1s

for _ in range(0, check_number, 1):
  test_result.append(process.cpu_percent(1))

summary = 0
for item in test_result:
  summary += item

average_cpu_usage = summary / len(test_result)

print("Total recorded data: {}".format(len(test_result)))
for cpu_usage in test_result:
  print("{:.0%}".format(cpu_usage))

print("CPU usage: {:.0%} in {} minutes".format(average_cpu_usage, check_time))

