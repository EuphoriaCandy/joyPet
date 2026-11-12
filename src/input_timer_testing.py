import msvcrt
import time

endtime = time.monotonic() + 10

while time.monotonic() < endtime:
    if msvcrt.kbhit():
        print("yeah I just got: " + str(msvcrt.getwch()))


