import csv
import random
import os

target_points = 220
simulations = 10000

def run_sim(velocity_sample):
    results = []
    for _ in range(simulations):
        rem = target_points
        sprints = 0
        while rem > 0:
            v = random.choice(velocity_sample)
            rem -= v
            sprints += 1
        results.append(sprints)
    results.sort()
    p50 = results[int(0.50 * simulations)]
    p85 = results[int(0.85 * simulations)]
    return p50, p85

possible_paths = [
    'lr09_reference_velocity.csv',
    '../lr09_reference_velocity.csv',
    '../../home_works/LR09 Прогноз velocity і Monte Carlo/lr09_reference_velocity.csv'
]

file_path = next((p for p in possible_paths if os.path.exists(p)), None)

if not file_path:
    file_path = input("Введіть шлях до файла lr09_reference_velocity.csv: ").strip()

velocities = []
with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        velocities.append(int(row['points_done']))

p50_all, p85_all = run_sim(velocities)
p50_12, p85_12 = run_sim(velocities[:2])
p50_56, p85_56 = run_sim(velocities[4:6])

print("\n--- Отримані числа для Розділу 5 README ---")
print(f"Усі 12 спринтів:   P50 = {p50_all}, P85 = {p85_all}")
print(f"Спринти 1 і 2:      P50 = {p50_12}, P85 = {p85_12}")
print(f"Спринти 5 і 6:      P50 = {p50_56}, P85 = {p85_56}")