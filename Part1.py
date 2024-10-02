import pandas as pd

data = {
    'Набор А': [85, 90, 95, 100, 105],
    'Набор Б': [70,80,95,110,120]
}

df = pd.DataFrame(data)

stdA = df['Набор А'].std()
stdB = df['Набор Б'].std()

print(f"стандартное отклонение набор А - {stdA}")
print(f"стандартное отклонение набор Б - {stdB}")