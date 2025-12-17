import numpy as np

# 1. Generate Data
sample_scores = np.random.randint(0, 101, size=10)
print("--- Sample Scores ---")
print(sample_scores)

# 2. Statistics
mean_score = np.mean(sample_scores)
median_score = np.median(sample_scores)
std_deviation = np.std(sample_scores)

print(f"Class Average (Mean): {mean_score:.2f}")
print(f"Median Score: {median_score}")
print(f"Standard Deviation: {std_deviation:.2f}")

# 3. Define Conditions (The Tricky Part)
# IMPORTANT: You MUST use parentheses () around every comparison when using &
conditions = [
    (sample_scores >= mean_score + std_deviation),           # A
    (sample_scores >= mean_score) & (sample_scores < mean_score + std_deviation), # B
    (sample_scores >= mean_score - std_deviation) & (sample_scores < mean_score), # C
    (sample_scores < mean_score - std_deviation)             # D
]

# 4. Define Choices
choices = ['A', 'B', 'C', 'D']

# 5. Apply Logic
letter_grades = np.select(conditions, choices, default='F')

# 6. Print Results
print("\n--- Student Results ---")
for i in range(10):
    print(f"Student {i+1}: Score = {sample_scores[i]}, Grade = {letter_grades[i]}")