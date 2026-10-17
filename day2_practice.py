# Day 2 - Python for Robot Decision Making

# Simulated ultrasonic sensor readings (in cm)
distances = [45, 30, 12, 60, 8, 25, 18]

print("All sensor readings:", distances)
print("-" * 40)

# Loop through each reading and decide
print("Obstacle Check:")
for d in distances:
    if d < 15:
        print(f"{d} cm → STOP + REVERSE (Obstacle very close)")
    elif d < 30:
        print(f"{d} cm → SLOW DOWN (Caution)")
    else:
        print(f"{d} cm → CONTINUE (Path clear)")

print("-" * 40)

# Same logic written as a function
def decide_action(distance):
    if distance < 15:
        return "STOP_AND_REVERSE"
    elif distance < 30:
        return "SLOW_DOWN"
    else:
        return "CONTINUE"

print("Using function:")
for d in distances:
    action = decide_action(d)
    print(f"Distance {d} cm → Action: {action}")

