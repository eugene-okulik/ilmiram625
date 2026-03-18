from datetime import datetime
import time

life_time = 5
sec_time = 0

while sec_time < life_time:
    print(f'Hello from docker! Time is {datetime.now()}')
    sec_time += 1
    time.sleep(2)
	