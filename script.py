# Generate random DNA sequence

import random

length = 50
DNA = random.choices("ATCG", k=length)
print("".join(DNA))
