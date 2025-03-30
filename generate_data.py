import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic student data
num_students = 500

data = {
    'SGPA_Sem1': np.random.uniform(5.0, 10.0, num_students),
    'SGPA_Sem2': np.random.uniform(5.0, 10.0, num_students),
    'SGPA_Sem3': np.random.uniform(5.0, 10.0, num_students),
    'SGPA_Sem4': np.random.uniform(5.0, 10.0, num_students),
    'Attendance': np.random.uniform(50, 100, num_students),
    'Study_Hours': np.random.uniform(1, 10, num_students),
    'Extracurricular': np.random.choice([0, 1], num_students),  # 0 = No, 1 = Yes
    'Backlogs': np.random.randint(0, 5, num_students),  # Number of backlogs
}

# Calculate CGPA as the average of SGPA values
df = pd.DataFrame(data)
df['CGPA'] = df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4']].mean(axis=1)

# Save dataset to CSV
df.to_csv("student_data.csv", index=False)

print("Synthetic dataset created successfully!")
print(df.head())
