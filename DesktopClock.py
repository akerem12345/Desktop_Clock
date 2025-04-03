import datetime
import time

print("=======================================================================")
print("                          Desktop Clock")
print("=======================================================================")

today = datetime.date.today().strftime("%d/%m/%y")
print(today)

while(1):
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\r{timenow}", end="", flush=True)
    time.sleep(1)