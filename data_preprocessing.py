# Load dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\Pragya\Desktop\CGPA\student_data.csv")


# Check for missing values
print(df.isnull().sum())

# Normalize numerical features

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours']] = scaler.fit_transform(
    df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours']]
)

# Split data into features (X) and target (Y)
X = df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours', 'Extracurricular']]
y = df['CGPA']

# Split into training & testing sets (80-20)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data Preprocessing Completed!")
