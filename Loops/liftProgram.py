import time
for floor in range(1, 21):
    if floor == 13:
        print("Skipping floor 13...")
        break
    print("Lift at floor:", floor)
    time.sleep(1)