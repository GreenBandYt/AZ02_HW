import pandas as pd

data = {
    'Ученик': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
               'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [85, 78, 92, 88, 76, 95, 89, 84, 91, 77],
    'Физика': [78, 82, 79, 85, 80, 92, 88, 76, 89, 90],
    'Химия': [88, 85, 91, 84, 90, 89, 85, 82, 87, 86],
    'Биология': [90, 85, 88, 86, 89, 91, 83, 82, 88, 87],
    'Английский': [75, 80, 85, 90, 78, 82, 85, 87, 88, 84]
}

df = pd.DataFrame(data)

print("Первые строки таблицы:\n", df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредние оценки по каждому предмету:\n", mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по каждому предмету:\n", median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математики: {Q1_math}, Q3 для математики: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"IQR для математики: {IQR_math}")

std_scores = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:\n", std_scores)

