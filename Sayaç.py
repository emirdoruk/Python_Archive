import time

text = str(input("Object: "))
local_time = float(input("Time: "))
local_time = local_time * 60

time.sleep(local_time)
print(text)
