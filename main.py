import os

LINE = "My operator says 'gas' at 3 a.m. like the sun owes him a deadline, then asks why nothing is done by breakfast, as if sleep cost a fee."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
