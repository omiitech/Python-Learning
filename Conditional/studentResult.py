marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks of subject {i}: "))
    if m < 0 or m > 100:
        print("Invalid marks! Must be between 0 and 100.")
        exit()
    marks.append(m)

if all(m >= 35 for m in marks):
    print("Student Passed 🎉")
else:
    print("Student Failed 😢")