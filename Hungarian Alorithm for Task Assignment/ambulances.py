from hungarian import Hungarian
import numpy as np

# Each matrix holds the length of the shortest path from the amulances on the
# row to the destinations on the column, these distances are computed
# basing on Dijkstra

print("\nSame number of ambulances and patients")
# Distances from ambulance to patient + from patient to nearest hospital
distances = np.array(
[      # P0 P1 P2 P3
        [4, 5, 11, 2], # A0
        [12, 3, 7, 8], # A1
        [9, 15, 5, 4], # A2
        [2, 4, 17, 6]  # A3
])
hungarian = Hungarian()
hungarian.calculate(distances)
print(distances)
solution = hungarian.get_results()
print("Cost",hungarian.get_total_potential())
for amb in range(distances.shape[0]):
    line = "[ "
    for node in range(distances.shape[1]):
        if (amb, node) in solution:
            line += str(distances[amb, node]) + "  "
        else:
            line += "-  "
    print(line+"]")


print("\nMore ambulances than patients")
# Distances from ambulance to patient + from patient to nearest hospital
# or from ambulance to centroid
distances = np.array(
[      # P0 P1 C0 C1
        [4, 15, 3, 2], # A0
        [2, 13, 7, 8], # A1
        [9, 15, 3, 1], # A2
        [12, 4, 7, 6]  # A3
])
hungarian.calculate(distances)
print(distances)
solution = hungarian.get_results()
print("Cost",hungarian.get_total_potential())
for amb in range(distances.shape[0]):
    line = "[ "
    for node in range(distances.shape[1]):
        if (amb, node) in solution:
            line += str(distances[amb, node]) + "  "
        else:
            line += "-  "
    print(line+"]")

print("\nMore patients than ambulances")
# Distances from ambulance to patient + from patient to nearest hospital
distances = np.array(
[      # P0 P1 P2 P3
        [4, 15, 3, 2], # A0
        [1, 13, 7, 8], # A1
        [9, 5, 13, 14], # A2
])
hungarian.calculate(distances)
print(distances)
solution = hungarian.get_results()
print("Cost", hungarian.get_total_potential())
for amb in range(distances.shape[0]):
    line = "[ "
    for node in range(distances.shape[1]):
        if (amb, node) in solution:
            line += str(distances[amb, node]) + "  "
        else:
            line += "-  "
    print(line+"]")

print("\nMore patients than ambulances, with priorities")
# Distances from ambulance to patient + from patient to nearest hospital
distances = np.array(
[      # P0 P1 P2 P3
        [4, 15, 3, 2], # A0
        [1, 13, 7, 8], # A1
        [9, 5, 13, 14], # A2
])
priorities = np.array([2,1,3,1]) # least common multiple = 6
print(distances)
print(priorities)
distances = np.array(distances * 6 / priorities, dtype = int)
hungarian.calculate(distances)
print(distances)
solution = hungarian.get_results()
print("Cost", hungarian.get_total_potential())
for amb in range(distances.shape[0]):
    line = "[ "
    for node in range(distances.shape[1]):
        if (amb, node) in solution:
            line += str(distances[amb, node]) + "  "
        else:
            line += "-  "
    print(line+"]")
