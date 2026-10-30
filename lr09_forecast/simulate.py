import math
import random

velocity = [18, 12]
simulations = 10000
remaining_points = 28

results = []
for _ in range(simulations):
    rem = remaining_points
    sprints = 0
    while rem > 0:
        v = random.choice(velocity)
        rem -= v
        sprints += 1
    results.append(sprints)

results.sort()

# Обчислення P50 та P85 за індексами
p50_sprints = results[int(0.50 * simulations)]
p85_sprints = results[int(0.85 * simulations)]

print(f"P50: {p50_sprints} sprints, P85: {p85_sprints} sprints")