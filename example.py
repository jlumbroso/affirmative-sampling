import collections
import math

from affirmative_sampling import affirmative_sampling
from affirmative_sampling.example import mobydick_tokens


print("""=====================================================
'Affirmative Sampling' by J. Lumbroso and C. Martínez
=====================================================
""")

# Example with Moby Dick (from the Gutenberg Project)
print("   Examples use Moby Dick (from the Gutenberg Project)")

tokens = mobydick_tokens[:]
N = len(tokens)
n = len(set(tokens))
k = 100

# print the size (N), the cardinality (n),
# and expected size of sample for the given k

print(f"   N={N}, n={n}, k={k}, k*ln(n/k)={k*math.log(n/k)+k}")


# Compute a random sample with Affirmative Sampling

sample = affirmative_sampling(tokens=tokens, k=k)


# =======================================
# EXAMPLE 1: Number of tokens without 'e'

TOTAL_number_of_tokens_without_e = len([
    token
    for token in set(tokens)
    if "e" not in token
])

SAMPLE_number_of_tokens_without_e = len([
    token
    for token in sample["sample"].keys()
    if "e" not in token
])

ESTIMATED_PROPORTION_number_of_tokens_without_e = (
    SAMPLE_number_of_tokens_without_e / sample["sampleSize"] * 100.0
)

ESTIMATED_number_of_tokens_without_e = (
    SAMPLE_number_of_tokens_without_e / sample["sampleSize"]
    * sample["cardinalityEstimate"]
)

print("""
EXAMPLE 1: Number of tokens without 'e'
====================================
- Exact count: {}
- Estimated count: {}
  - Error: {}%

- Size of sample: {}
   - Expected size of sample: {}
   - Tokens in sample without 'e': {}
   - Proportion of tokens in sample without 'e': {}%
""".format(
    TOTAL_number_of_tokens_without_e,
    round(ESTIMATED_number_of_tokens_without_e, 2),
    abs(round((ESTIMATED_number_of_tokens_without_e /
               TOTAL_number_of_tokens_without_e-1.0)*100.0, 2)),
    len(sample["sample"]),
    round(k*math.log(n/k)+k, 2),
    SAMPLE_number_of_tokens_without_e,
    round(ESTIMATED_PROPORTION_number_of_tokens_without_e, 2),
))


# =======================================================================================
# EXAMPLE 2: Number of mice (rare elements, i.e., elements with freq. less or equal to 5)

MICE_THRESHOLD = 5

TOTAL_number_of_distinct_mice = len([
    token
    for (token, count) in collections.Counter(mobydick_tokens).items()
    if count <= 5
])

SAMPLE_number_of_distinct_mice = len([
    token
    for (token, count) in sample["sample"].items()
    if count <= 5
])

ESTIMATED_PROPORTION_number_of_distinct_mice = (
    SAMPLE_number_of_distinct_mice / sample["sampleSize"] * 100.0
)

ESTIMATED_number_of_distinct_mice = (
    SAMPLE_number_of_distinct_mice / sample["sampleSize"]
    * sample["cardinalityEstimate"]
)

print("""
EXAMPLE 2: Number of mice (freq. less or equal to {})
====================================================
- Exact count: {}
- Estimated count: {}
  - Error: {}%

- Size of sample: {}
   - Expected size of sample: {}
   - Number of mice in sample: {}
   - Proportion of mice in sample: {}%
""".format(
    MICE_THRESHOLD,
    TOTAL_number_of_distinct_mice,
    round(ESTIMATED_number_of_distinct_mice, 2),
    abs(round((ESTIMATED_number_of_distinct_mice /
               TOTAL_number_of_distinct_mice-1.0)*100.0, 2)),
    len(sample["sample"]),
    round(k*math.log(n/k)+k, 2),
    SAMPLE_number_of_distinct_mice,
    round(ESTIMATED_PROPORTION_number_of_distinct_mice, 2),
))


# Outputting the full sample

print("SAMPLE")
print("======")
for (token, count) in sorted(sample["sample"].items(), key=lambda pair: (-pair[1], pair[0])):
    print(f"{count:>5} {token} ")
