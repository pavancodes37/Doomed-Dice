from collections import defaultdict
import itertools
import numpy as np

def calculate_distribution(die_a, die_b):
    """Calculate sum distribution and probabilities."""
    distribution = defaultdict(int)
    total_combinations = len(die_a) * len(die_b)
    
    for a, b in itertools.product(die_a, die_b):
        distribution[a + b] += 1
    
    probabilities = {k: v / total_combinations for k, v in distribution.items()}
    
    return distribution, probabilities, total_combinations

def undoom_dice(die_a, die_b):
    """Transform dice to satisfy Loki's conditions while keeping probabilities the same."""
    _, original_probabilities, _ = calculate_distribution(die_a, die_b)
    
    # Define new Die A within constraints (max 4 spots per face)
    new_die_a = [1, 1, 2, 2, 3, 4]  # Example valid transformation
    
    # Solve for new Die B
    new_die_b = [0] * 6
    sum_counts = defaultdict(int)
    
    for a in new_die_a:
        for sum_val, prob in original_probabilities.items():
            expected_count = prob * 36  # Convert probability back to counts
            if sum_counts[sum_val] < expected_count:
                new_die_b[new_die_a.index(a)] = sum_val - a
                sum_counts[sum_val] += 1
    
    return new_die_a, new_die_b

def create_sum_matrix(die_a, die_b):
    """Create a 6x6 matrix for sum distribution."""
    sum_matrix = np.zeros((6, 6), dtype=int)
    for i in range(6):
        for j in range(6):
            sum_matrix[i][j] = die_a[i] + die_b[j]
    return sum_matrix

# Part A - Original Dice
original_die_a = [1, 2, 3, 4, 5, 6]
original_die_b = [1, 2, 3, 4, 5, 6]

distribution, probabilities, total_combinations = calculate_distribution(original_die_a, original_die_b)
print("Total possible combinations:", total_combinations)
print("Sum Distribution:", distribution)
print("Probabilities:", probabilities)

# Sum Distribution Matrix
sum_matrix = create_sum_matrix(original_die_a, original_die_b)
print("Sum Distribution Matrix:")
print(sum_matrix)

# Part B - Transformed Dice
new_die_a, new_die_b = undoom_dice(original_die_a, original_die_b)
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
