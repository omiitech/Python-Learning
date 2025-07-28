import time

print("🚀 Lift Program Started 🚀")

for floor in range(1, 21):
    if floor == 13:
        print("Skipping floor 13...")
        break   # stops the lift after printing 'Skipping floor 13'
    print(f"Lift is at floor {floor}")
    time.sleep(1)

print("⛔ Lift stopped at floor 13.")
